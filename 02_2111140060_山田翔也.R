install.packages("twitteR", dependencies = TRUE)
install.packages("RMeCab", repos = "http://rmecab.jp/R",dependencies = TRUE)
library(twitteR)
library(RMeCab)
library(ggplot2)

data<-read.csv("�Y�ƍ\���}�b�v_�ٗp_��l���������_�s���{��_�S�Y��.csv",fileEncoding  ="sjis")
head(data)

Fukuoka <-data[data$�N�� =="�N��v" & data$�s���{����=="������",]$��l���������.���~.
Fukuoka

Osaka <-data[data$�N�� =="�N��v" & data$�s���{����=="���{",]$��l���������.���~.
Osaka

tmp<-data.frame(������=Fukuoka,���{=Osaka)
tmp
