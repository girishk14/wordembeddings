import numpy as np
import matplotlib.pyplot as plt

la = np.linalg




def main():
	sentences = ["I like deep learning", "I love NLP", "I dont love my girlfriend", "I love Wonderwoman"]
	words, m = sent2covec(sentences)
	print(m)
	U, S, V_t = 	la.svd(m,full_matrices = False)
	
	for i in xrange(len(m)):
		plt.text(U[i,0], U[i,1],words[i])

	plt.show()

def sent2covec(sentences):
	word_list = sorted(set([word.lower() for sent in sentences for word in sent.split()]))
	invmap = {}
	for idx, word in enumerate(word_list):
		invmap[word] = idx
	covec = np.zeros([len(word_list), len(word_list)])
	
	print(word_list)

	for sent in sentences:
		words = [w.lower() for w in sent.split()]
		for idx,word in enumerate(words):

			if idx - 1 >= 0:
				covec[invmap[word]][invmap[words[idx-1]]] +=1

		
			
			if idx + 1 < len(words):
				covec[invmap[word]][invmap[words[idx+1]]] +=1

	

	return word_list,covec
if __name__ == "__main__":
	main()
