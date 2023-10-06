data_02<-read.csv("Y‹Æ\‘¢_‘SY‹Æ_‘SY‹Æ‚Ì\‘¢_Šé‹Æ”_“s“¹•{Œ§_‘S‹Æí.csv",fileEncoding  ="sjis")
head(data_02)
data_02

my_summary <- function(data1, data2, label1, label2, y_label) {
  # (1) ” ‚Ğ‚°}‚Ì•`‰æ
  boxplot(list(Data1=data1, Data2=data2), xlab="Data", ylab=y_label, names=c(label1, label2))
  
  # (2) Šeƒf[ƒ^‚Ì•½‹Ï’lAÅ‘å’lAÅ¬’l‚ğŒvZ
  summary_data <- data.frame(
    Label = c(label1, label2),
    Mean = c(mean(data1), mean(data2)),
    Max = c(max(data1), max(data2)),
    Min = c(min(data1), min(data2))
  )
  
  return(summary_data)
}

my_summary(data_02[data_02$WŒv”N==2009, ]$Šé‹Æ”,data_02[data_02$WŒv”N==2012, ]$Šé‹Æ”, "2009", "2012","Šé‹Æ”")

data_2009 <- data$`2009”N`
data_2012 <- data$`2012”N`

result <- my_summary(data_2009, data_2012, "2009", "2012", "Šé‹Æ”")
print(result)