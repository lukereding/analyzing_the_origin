## make a word cloud of the most common 1000 words

# install.packages("wordcloud")
# install.packages("tm")

library(tm)
library(wordcloud)
library(magrittr)
library(wesanderson)

origin <- Corpus(DirSource("~/Desktop/analyzingTheOrigin/origin/"))

origin %<>% 
  tm_map(stripWhitespace) %>%
  tm_map(tolower) %>%
  tm_map(removeWords, stopwords("english")) %>%
  tm_map(removeNumbers) %>%
  tm_map(removePunctuation) %>%
  tm_map(PlainTextDocument)

wordcloud(origin, 
          scale=c(3,0.5), 
          max.words=200, 
          random.order=FALSE, 
          use.r.layout=FALSE, 
          random.color = TRUE,
          colors=wes_palette("Moonrise2"))


##########

x<-read.csv("~/Desktop/analyzingTheOrigin/wordsBySentence.csv")
str(x)
names(x) <- c("position","sentenceLength","wordLength")


plot(x$position,x$wordLength)
# starting poisitions of each chapter
chapters <- c(59,416,574,753,1183,1534,1822,2151,2458,2732,3016,3578,3977)

# for plotting the points in alternative colors:
for(i in 1:(length(chapters))){
  y = chapters[i]
  z = chapters[i+1]
  print(y)
  
  # for the last chapter
  if(i == length(chapters)){
    points(x$position[y:4250],x$wordLength[y:4250],col="black",pch=16)
  }
  
  # if i is odd:
  else if(i%%2==1){
    points(x$position[y:z],x$wordLength[y:z],col="black",pch=16)
  }
  
  # if i is even:
  else{
    points(x$position[y:z],x$wordLength[y:z],col="grey70",pch=16)
  }
}


### most common words
words <- read.csv("/Users/lukereding/Desktop/mostCommonWords.csv")
head(words)
names(words)<-c("word","count")
hist(log(words$count))


