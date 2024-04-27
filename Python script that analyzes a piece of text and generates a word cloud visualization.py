from wordcloud import WordCloud
import matplotlib.pyplot as plt

def generate_word_cloud(text):
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()

def main():
    print("Welcome to the Word Cloud Generator!")
    text = input("Enter the text you'd like to analyze: ")
    generate_word_cloud(text)

if __name__ == "__main__":
    main()
