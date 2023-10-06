install.packages("twitteR", dependencies = TRUE)
install.packages("RMeCab", repos = "http://rmecab.jp/R",dependencies = TRUE)
library(twitteR)
library(RMeCab)
library(ggplot2)

data<-read.csv("ŽY‹Æ\‘¢ƒ}ƒbƒv_ŒÙ—p_ˆêl“–‚½‚è’À‹à_“s“¹•{Œ§_‘SŽY‹Æ.csv",fileEncoding  ="sjis")
head(data)

Fukuoka <-data[data$”N—î =="”N—îŒv" & data$“s“¹•{Œ§–¼=="•Ÿ‰ªŒ§",]$ˆêl“–‚½‚è’À‹à.–œ‰~.
Fukuoka

Osaka <-data[data$”N—î =="”N—îŒv" & data$“s“¹•{Œ§–¼=="‘åã•{",]$ˆêl“–‚½‚è’À‹à.–œ‰~.
Osaka

tmp<-data.frame(•Ÿ‰ªŒ§=Fukuoka,‘åã•{=Osaka)
tmp
