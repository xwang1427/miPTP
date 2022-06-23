library('optparse')
library('Biostrings')
library('stringr')

option_list = list(
  make_option(c("-i", '--inputfile'), type = 'character', default = FALSE, help = 'input the result file of second-level prediction'),
  make_option(c('-x', '--genePromfile'), type = 'character', default = FALSE, help='input the x'),
  make_option(c('-o', '--outfile'), type = 'character', default = FALSE, help='output file for saving results')
)
opt_parser = OptionParser(option_list=option_list)
opt = parse_args(opt_parser)

inputfile = opt$inputfile
x = opt$genePromfile
outPath = opt$outfile

RFpred.Promoter = read.csv(inputfile, header = F)
# genePromoters
load(x)
p_thre = 0.853
s_thre = 0.759
# calculate gene-miRNA, (Pearson, Spearman, Maxnum)
miName.Freq =  as.data.frame(table(RFpred.Promoter[ ,1]))
for (i in 1:nrow(miName.Freq))
{
  best_row = -1
  p.num_upp = c()
  s.num_upp = c()
  max4bin = c() 
  locSub = which(RFpred.Promoter[ ,1] == miName.Freq[i, 1]) 
  sub.miStart = locSub[1]
  sub.miEnd = locSub[1] + miName.Freq[i,2] - 1
  z = t(RFpred.Promoter[sub.miStart:sub.miEnd, 6:16]) #11 bins
  Pearson_gm = cor(x,z)  
  Spearman_gm = cor(x,z,method = 'spearman')
  
  for(j in 1:miName.Freq[i,2]) 
  {
    p.num_upp[j] = length(which(Pearson_gm[ ,j] >= p_thre))
    s.num_upp[j] = length(which(Spearman_gm[ ,j] >= s_thre))
    
    rowIndex = locSub[j]
    max4bin[j] = max(RFpred.Promoter[rowIndex,10:13])  #4 bins
  }
  subdata = data.frame(p.num_upp,s.num_upp, max4bin) 
  subdata = subset(subdata, p.num_upp>=50 & s.num_upp>=50) 
  
  if(nrow(subdata) != 0)
  {
    rowIndex = as.numeric(c(rownames(subdata))) 
    best_rows = c(locSub[rowIndex])
    miRNA_OptimalPromoter = RFpred.Promoter[best_rows, ]
    write.table(miRNA_OptimalPromoter[ ,1:5], file=outPath, sep='\t', row.names = F, col.names = F, quote = F, append = T)
  }
  # print(i)
}
print('Third-level prediction finished!')





