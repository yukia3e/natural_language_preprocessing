"""
Preprocessing Utils
"""
import re
import string
from bs4 import BeautifulSoup
from collections import Counter

# 日本語判定
def filter_by_ascii_rate(text, threshold=0.9):
  ascii_letters = set(string.printable)
  rate = sum(c in ascii_letters for c in text) / len(text)
  return rate <= threshold

# HTMLタグ除去
def clean_html(html, strip=False):
  soup = BeautifulSoup(html, 'html.parser')
  text = soup.get_text(strip=strip)
  return text


# aタグ除去
def remove_url(html):
  soup = BeautifulSoup(html, 'html.parser')
  for a in soup.findAll('a'):
    a.replaceWithChildren()
  return str(soup)


# 数字の置き換え
def normalize_number(text, reduce=False):
  if reduce:
    normalized_text = re.sub(r'\d+', '0', text)
  else:
    normalized_text = re.sub(r'\d', '0', text)
  return normalized_text


# 小文字化
def lower_text(text):
  return text.lower()


# 大文字化
def upper_text(text):
  return text.upper()


# ストップワード除去（辞書ベース）
def remove_stopwords(words_array, stopwords_array):
  words = [w for w in words_array if w not in stopwords_array]
  return words


# ストップワード除去（出現頻度）
def create_stopwords_based_count(words_array, n=10):
  fdist = Counter(words_array)
  return [w for w, _ in fdist.most_common(n=n)]
