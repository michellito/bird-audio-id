from fastmcp import FastMCP

import birdnet
import librosa
import soundfile as sf

from typing import List, Dict, Any
from pathlib import Path

# 1. Instantiate the MCP server
mcp = FastMCP(name="birdnet_server")

# 2. Define function for converting multi-channel audio to mono-channel
def batch_convert_to_mono(file_list):
    mono_files = []
    
    for file_path in file_list:
        file_path = Path(file_path)
        
        # Load and convert to mono
        audio, sr = librosa.load(file_path, mono=True)
        
        # Create output filename
        mono_file = file_path.parent / f"{file_path.stem}_mono{file_path.suffix}"
        
        # Save mono version
        sf.write(mono_file, audio, sr)
        mono_files.append(mono_file)
        print(f"Converted {file_path} -> {mono_file}")
    
    return mono_files

# 3. Define the BirdNET tool for analyzing audio
@mcp.tool()
def analyze_audio_for_species(audio_file_paths: List[str]) -> List[Dict[str, Any]]:
    """
    Analyzes the specified audio files for bird species using BirdNET.
    It uses librosa to convert stereo files to mono before analysis.

    :param audio_file_paths: A list of paths to the audio files (e.g., .wav, .mp3) to analyze.
    :return: A list of analysis results, where each element contains predictions 
             for one of the input audio files.
    """
    print(f"Starting BirdNET analysis for {len(audio_file_paths)} file(s)...")

    mono_files = batch_convert_to_mono(audio_file_paths)

    try:
        predictions = birdnet.predict_species_within_audio_files_mp(
          mono_files
        )
        return predictions
    except Exception as e:
        # IMPORTANT: Return a useful error message to the LLM
        return [{"error": f"An error occurred during BirdNET analysis: {e}"}]


# 4. Define the location-based prediction tool
@mcp.tool()
def predict_species_by_location(
    latitude: float, 
    longitude: float, 
    week: int
) -> Dict[str, float]:
    """
    Predicts bird species likely to be found at a specific geographic location and time of year.
    Returns species predictions based on occurrence patterns, not audio analysis.
    
    :param latitude: Latitude coordinate (e.g., 42.5 for Ithaca, NY or 32.2319 for Tucson, AZ)
    :param longitude: Longitude coordinate (e.g., -76.45 for Ithaca, NY or -110.9501 for Tucson, AZ)
    :param week: Week of the year (1-48, where 1 = first week of January, 48 = last week of November)
    :return: Dictionary of species names mapped to confidence scores (0.0 to 1.0), 
             sorted by confidence in descending order. Species names are in format 
             'Scientific_name_Common Name' (e.g., 'Cyanocitta cristata_Blue Jay').
    """
    try:
        print(f"Predicting species for location ({latitude}, {longitude}) during week {week}...")
        
        prediction = birdnet.predict_species_at_location_and_time(latitude, longitude, week=week)
        
        return prediction
        
    except Exception as e:
        return {"error": f"An error occurred during location-based prediction: {e}"}
    

# 5. The server entry point
if __name__ == "__main__":
    mcp.run(transport="http", host="127.0.0.1", port=8000)
    # mcp.run()