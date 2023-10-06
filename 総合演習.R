object<-read.csv("C:/Class_R/Class/object.csv")
averave_object <- colMeans(object[,c("英語","現文","数学")])
barplot(averave_object,ylim=c(0,100),xlab="科目",ylab="平均点",name.arg=c("英語","現文","数学"))

my_object<-function(object, y_label, x_label, y_min, y_max){
  average_scores <- colMeans(object[,c("英語","現文","数学")])
  barplot(average_scores, ylim = c(y_min, y_max),xlab = x_label, ylab = y_label, names.arg =c("英語","現文","数学"))
}
my_object(object,"平均点","科目",0,100)

library(RMeCab)
library(dplyr)
library(stringr)
word <- read.table("tyawa.txt", fileEncoding="UTF-8")
str(word)
head(word)
data%>%head()
word %>% str_count("茶わん") %>% sum()
sentences <- unlist(strsplit(as.character(word$V1), split = "。"))
for (sentence in sentences) {
  if (grepl("茶わん", sentence)) {
    start_index <- grep("茶わん", sentence)
    extracted_text <- substr(sentence, start_index, nchar(sentence))
    print(extracted_text)
  }
}

print(word)

calculate_document <- function(document, target_word){
  tokens <- unlist(strsplit(document, split = " "))
  cooccurring_count <- sum(tokens == target_word)
  total_tokens <- length(tokens)
  other_tokens <- total_tokens - cooccurring_count
  p_target <- cooccurring_count / total_tokens
  p_other <- other_tokens / total_tokens
  t_value <- (cooccurring_count / total_tokens) / (cooccurring_count / other_tokens)
  mi_value <- log2(p_target / (p_target + p_other))
  return(list(T_value = t_value, MI_value = mi_value))
}
Hulk <- read.csv("C:/Class_R/Class/Hulk.txt")
print(Hulk)
document<-Hulk$X1[0:184]
print(document)
target_word <- "ソロドフニコフ"

# T値とMI値を計算して表示
results <- calculate_document(document, target_word)
print(paste("T値:", results$T_value))
print(paste("MI値:", results$MI_value))


  
library(rvest)
library(xml2)
url <- read_html("https://www.uta-net.com/song/244127/")
 # 歌詞を抽出
lyric <- html_nodes(url, "div#kashi_area")
 # 何個のノードが取得できたかチェック(1個ならそのまま扱い,複数ならどれが所望のデータか見極める)
length(lyric)
lyric
# テキストの抽出
text <- html_text(lyric)
# テキストの抽出
text <- html_text(lyric)
text

url_01 <- read_html("https://ranking.net/rankings/best-popular-avengers-movies")
# 歌詞を抽出
lyric_01 <- html_nodes(url_01, "td.py-1")
# 何個のノードが取得できたかチェック(1個ならそのまま扱い,複数ならどれが所望のデータか見極める)
length(lyric_01)
lyric_01
# テキストの抽出
text_01 <- html_text(lyric_01)
# テキストの抽出
text_01 <- html_text(lyric_01)
text_01
