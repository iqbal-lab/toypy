import numpy as np
import scipy
import pandas
import h5py
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('white')
sns.set_style('ticks')
import allel;
import pprint


# Playing with basic Python and scikit-allel
# Ideas from http://alimanfoo.github.io/2017/06/14/read-vcf.html


#made up VCF based on a real plasmodium VCF. Samples are called
# GB4 and mickeymouse
callset = allel.read_vcf('test.vcf')

gt = allel.GenotypeArray(callset['calldata/GT'])

#how many sites are not SNPs?

ref = callset['variants/REF']
alt = callset['variants/ALT']
non_snp=0;
snp=0;
for i in range(len(ref)):
    if ( (len(ref[i])>1) and (len(alt[i])>1)):
        snp=snp+1
    else:
        non_snp=non_snp+1

print("There are",snp,"SNPs and",non_snp, "indels")

#how many sites do MickeyMouse and  GB4 differ?

genotypes_equal = np.all(gt[:, 0] != gt[:, 1], axis=1)
print(genotypes_equal)


varinfo = allel.read_vcf('test.vcf', fields='variants/*')
print(sorted(varinfo.keys()))

callinfo = allel.read_vcf('test.vcf', fields='calldata/GT_CONF')

#just check we can count the high confidence calls
gt_high = np.all(callinfo['calldata/GT_CONF']>200, axis=1)
#no we cannot - why does this not work?
print(np.sum(gt_high))


#what is the distribution of genotype confidences?

plt.hist(callinfo["calldata/GT_CONF"],bins=[0,100,200,300,400,500])
plt.show()