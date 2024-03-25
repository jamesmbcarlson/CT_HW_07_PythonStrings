# James Carlson 
# Coding Temple - SE FT-144
# Backend Lesson 6 Assignment: Python Strings

print("\n=== 1. Product Review Analysis ===\n")

reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]

# Task 1 - Keyword Highlighter

keywords = ["good", "excellent", "bad", "poor", "average"]
highlighted_reviews = reviews.copy()

# replace found keywords with all-caps
for review in highlighted_reviews:
    for word in keywords:
        review = review.replace(word.capitalize(), word.upper())    # handles capitalized keywords
        review = review.replace(word, word.upper())                 # handles lowercase keywords
    print(review)
print()

# Task 2 - Sentiment Tally

# initializes keywords and tallies
positive_tally_total, positive_tally = 0, 0
negative_tally_total, negative_tally = 0, 0
positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

for review in reviews:
    # check each review for positive reviews
    for word in positive_words:
        positive_tally += review.casefold().count(word)

    # check each review for negative reviews
    for word in negative_words:
        negative_tally += review.casefold().count(word)
    
    # display each review and its keyword tally
    print(review)
    print("Positive keywords:", positive_tally)
    print("Negative keywords:", negative_tally, "\n")

    # increment totals and reset individual tallies
    positive_tally_total += positive_tally
    negative_tally_total += negative_tally
    positive_tally, negative_tally = 0, 0

# display final tallies
print(f"Positive keywords across all reviews: {positive_tally_total}")
print(f"Negative keywords across all reviews: {negative_tally_total}\n")

# Task 3 - Review Summary

summary_reviews = reviews.copy()

for review in summary_reviews:
    # find first space at or after character #30
    i = 29
    while review[i] != " ":
        i += 1
    # remove characters after i and add ellipsis
    review = review[:i]
    review += "..."
    print(review)