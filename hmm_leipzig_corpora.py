DEBUG = False

sentences_10k_path = './pt_corpus_10K/por-br_newscrawl_2011_10K-sentences.txt'
sentences_30k_path = './pt_corpus_30K/por-br_newscrawl_2011_30K-sentences.txt'
sentences_100k_path = './pt_corpus_100K/por_newscrawl_2011_100K-sentences.txt'
sentences_300k_path = './pt_corpus_300K/por_newscrawl_2011_300K-sentences.txt'
sentences_1M_path = './pt_corpus_1M/por_newscrawl_2011_1M-sentences.txt'

from HMM import MarkovChain

if DEBUG:
    import random

def main():
    word_list = []
    with open(sentences_1M_path, 'r', encoding='utf-8') as file:
        for line in file:
            _, sentence = line.strip().split('\t', 1)
            words = sentence.split()
            word_list.extend(words)

    markov_chain = MarkovChain(word_list, 2)
    # markov_chain_2 = MarkovChain(word_list, 2)

    sequence_examples = markov_chain.get_sequence_examples(5)
    print(sequence_examples)

    while True:
        choice = input('\n\n1 - generate text\n2 - generate with multiple chains (terminated)\n3 - exit\n')
        if choice == '1':
            generated_text = markov_chain.generate_text(start=input('Choose a starting sequence with '+str(markov_chain.n_gram)+' words\n'), limit=10)
            print(generated_text)
        if choice == '2':
            # generated_text = markov_chain.generate_text_with_multiple_chains(markov_chain_2, start=input('Choose a starting sequence with '+str(markov_chain.n_gram)+' words\n'), limit=10)
            # print(generated_text)
            continue
        elif choice == '3':
            break
        else:
            print('\nPlease insert a valid number\n')

if __name__ == '__main__':
    main()