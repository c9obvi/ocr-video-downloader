import os
import subprocess

def download_video(url, download_path, filename):
    try:
        # Ensure the download directory exists
        os.makedirs(download_path, exist_ok=True)
        
        # Append the .mp4 extension if not provided
        if not filename.endswith('.mp4'):
            filename += '.mp4'
        
        # Build the yt-dlp command
        cmd = [
            'yt-dlp',
            url,
            '-o',
            os.path.join(download_path, filename),
            '--format',
            'mp4'
        ]
        
        # Execute the command
        subprocess.run(cmd, check=True)
        print(f"Video downloaded successfully to {download_path}/{filename}")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

def main():
    # Prompt the user for the video URL and filename
    url = input("Enter the URL of the video: ")
    filename = input("Enter the desired filename (without extension): ")
    download_video(url, "/Users/your-username/path", filename)

if __name__ == "__main__":
    main()