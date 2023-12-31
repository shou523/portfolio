data_02<-read.csv("産業構造_全産業_全産業の構造_企業数_都道府県_全業種.csv",fileEncoding  ="sjis")
head(data_02)
data_02

my_summary <- function(data1, data2, label1, label2, y_label) {
  # (1) 箱ひげ図の描画
  boxplot(list(Data1=data1, Data2=data2), xlab="Data", ylab=y_label, names=c(label1, label2))
  
  # (2) 各データの平均値、最大値、最小値を計算
  summary_data <- data.frame(
    Label = c(label1, label2),
    Mean = c(mean(data1), mean(data2)),
    Max = c(max(data1), max(data2)),
    Min = c(min(data1), min(data2))
  )
  
  return(summary_data)
}

my_summary(data_02[data_02$集計年==2009, ]$企業数,data_02[data_02$集計年==2012, ]$企業数, "2009", "2012","企業数")

data_2009 <- data$`2009年`
data_2012 <- data$`2012年`

result <- my_summary(data_2009, data_2012, "2009", "2012", "企業数")
print(result)