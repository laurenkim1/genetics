import numpy as np

##################################
########## SETTINGS ##############
##################################

chromosome_num = 4
num_snps = 10000
conditions_fn = '../data/y_list.csv'
snp_unknown_fn = '../data/chromosome%d.csv' % (chromosome_num)

##################################
##################################


# get if patients have diabetes
num_diabetes = 0
num_not_diabetes = 0
patient_diabetes_dict = {}

f = open(conditions_fn, 'rU')
next(f)
for line in f:
	# print 'hi'
	# print line.split(',')
	sp_l = line.split(',')
	diabetes = int(sp_l[5])
	patient_id = sp_l[1]

	patient_diabetes_dict[patient_id] = diabetes

	if diabetes == 1:
		num_diabetes += 1
	else:
		num_not_diabetes += 1

print num_diabetes
print num_not_diabetes


f = open(snp_unknown_fn, 'rU')
first_flag = True
snp_number = 0

idx_to_patientid = {}



# get snp information

for line in f:
	if first_flag:
		patient_snp_feature = np.zeros((len(line.split(',')[2:]),num_snps))
		for i, patient_id in enumerate(line.split(',')[2:]):
			idx_to_patientid[i] = patient_id 
		first_flag = False
	else:
		for i, snp_feature in enumerate(line.split(',')[2:]):
			patient_snp_feature[i, snp_number] = int(snp_feature)
		snp_number += 1

	if snp_number >= num_snps:
		break

print patient_snp_feature


ys = np.zeros((len(patient_diabetes_dict)))
for i in range(len(patient_diabetes_dict)):
	this_patient_id = idx_to_patientid[i].strip()
	ys[i] = patient_diabetes_dict[this_patient_id]


# save into numpy array
np.savez('xs_ys_%d.npz' % (chromosome_num), xs=patient_snp_feature, ys=ys)



