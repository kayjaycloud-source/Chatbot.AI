import nltk

def download_nltk_data():
    try:
        # Essential for tokenization
        nltk.download('punkt')
        nltk.download('punkt_tab')
        # Essential for cleaning text
        nltk.download('stopwords')
        # Download additional languages for stopwords
        # Languages: English, Spanish, French, German, Italian, etc.
        # This allows the chatbot to support multiple languages in the future
        print("NLTK data (punkt, stopwords) downloaded.")
    except Exception as e:
        print(f"Error downloading NLTK data: {e}")

if __name__ == "__main__":
    download_nltk_data()
