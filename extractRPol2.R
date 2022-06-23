library('optparse')
library('stringr')
library('Biostrings')

option_list = list(
  make_option(c("-i", '--inputfile'), type = 'character', default = FALSE, help = 'input the .txt file'),
  make_option(c('-p', '--pol2file'), type = 'character', default = FALSE, help='input the RPol2 data file'),
  make_option(c('-o', '--outfile'), type = 'character', default = FALSE, help='output file for saving Pol2 features')
)
opt_parser = OptionParser(option_list=option_list)
opt = parse_args(opt_parser)

pol2Path = opt$pol2file
inputfile = opt$inputfile
outPath = opt$outfile

load(pol2Path)
FirstLevel_predProm = read.table(inputfile, sep='\t')
# 11 bins
bed[ ,3] = bed[ ,2] + 500
chr = ''
bin=100
num.fragment = matrix(0,nrow = nrow(FirstLevel_predProm),ncol = 11)  
for (i in 1:nrow(FirstLevel_predProm))
{
  start = FirstLevel_predProm[i,4]
  end = FirstLevel_predProm[i,5]
  if(chr != as.character(FirstLevel_predProm[i,2]))
  {
    chr = as.character(FirstLevel_predProm[i,2])
    chr.bed = bed[bed[ ,1]==chr, ]
  }
  if(as.character(FirstLevel_predProm[i,3]) == '+')
  {
    ll = start-400 
    rr = end+300
    gene.chr.bed = chr.bed[!(chr.bed[,3]<=ll | chr.bed[,2]>=rr), ]
    for (j in 1:11) 
    {
      num.fragment[i,j] = nrow(gene.chr.bed[!(gene.chr.bed[,3]<=ll+bin*(j-1) | gene.chr.bed[,2]>=ll+bin*j), ])
    }
  }else{
    ll = start-300 
    rr = end+400 
    gene.chr.bed = chr.bed[!(chr.bed[,3]<=ll | chr.bed[,2]>=rr), ]
    for (j in 1:11) 
    {
      num.fragment[i,j] = nrow(gene.chr.bed[!(gene.chr.bed[,3]<=rr-bin*j | gene.chr.bed[,2]>=rr-bin*(j-1)), ])
    }
  }
  # print(i)
}
FirstPred_11bin = cbind(FirstLevel_predProm, num.fragment)
write.csv(FirstPred_11bin, outPath, row.names = FALSE, quote = F)
print('Finished!')




