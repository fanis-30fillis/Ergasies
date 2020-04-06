# -*- coding: utf-8 -*-

# συνάρτηση που δέχεται μια λίστα και διαγράφει τις διπλοεγγραφές
def remove_duplicates(lista):
	# για κάθε αριθμό από το 0 έως το μήκος της λιστας
	for i in range(len(lista)):
    	# αρχικοποιεί το δεικτη για να κάνει διαγραφές 
		cnt = i+1
	# οσο υπάρχουν αντικείμενα που δεν έχουν ελεγχθεί για διπλοεγγραφές
	while(cnt < len(lista)):
		# αν υπάρχει διπλοεγγραφή	
		if(lista[i] == lista[cnt]):
			# τη διαγράφει
			del lista[cnt]
			# μειώνει κατά 1 το δείκτη για να δείχνει το επόμενο γράμμα
			# εφόσον το τωρινό διαγράφεται
			cnt -= 1
		# τελος if
	# αυξάνει τον δίκτη
	cnt += 1
	# τελος while
	# τέλος for
	return
# τέλος συνάρτησης remove_duplicates


# ταξινομεί αύξουσα μια λιστα 
def sort_list(lista):
	# σημαία που σηματοδοτεί εάν η λίστα είναι τεξινομημένη
	sorted_flag = False
	# όσο δεν είναι ταξινομημένη η λίστα
	while(not sorted_flag):
		# θέτει τη λίστα ως ταξινομημένη
		sorted_flag = True
		# δεικτης που περνάει τη λίστα
		cnt_in = 0
		# οσο δεν έχει περάσει όλη τη λίστα
		while(cnt_in < len(lista)-1):
			# αν το τωρινό στοιχείο είναι μεγαλήτερο από το επόμενο
			if(lista[cnt_in] > lista[cnt_in+1]):
				# αλλάζει τις θέσεις
				lista[cnt_in], lista[cnt_in+1] = lista[cnt_in+1], lista[cnt_in]
				# κάνει τη σημαία false
				sorted_flag = False
			# αυξάνει τον δείκτη
			cnt_in += 1	
	# επιστρέφει από τη συνάρτηση
	return


# συνάρτηση που δέχεται μια λίστα και διαγράφει τις διπλοεγγραφές
def remove_duplicates_dict(dct):
	# παίρνει τα κλειδιά του λεξικού
	keys = list(dct.keys())
	# μετρητής που περνάει τα κλειδια
	cnt_key = 0
	# όσο δεν έχουν περαστεί όλα τα κλειδιά
	while (cnt_key < len(keys)):
		# αρχικοποιεί το 
		cnt_dct = cnt_key + 1
		# όσο δεν έχει τελειώσει το λεξικό
		while (cnt_dct < len(dct)):
			# αν δυο αντικείμενα είναι ιδια 
			if(dct[keys[cnt_key]] == dct[keys[cnt_dct]]):
				# σβήνει το ένα από τα δυο
				del dct[keys[cnt_dct]]
				# σβήνει το κλειδι του δεύτερου στοιχείου
				del keys[cnt_dct]
				# μειώνει το μετρητή του dictionary κατά 1 γιατι 
				# διαγράφηκε το αντικείμενο
				cnt_dct -= 1
			# τελος της if
		# αυξάνει το μετρητή του λεξικού
		cnt_dct += 1
		# τέλος της while που περνάει το λεξικό
		# αυξάνει τον μετρητή των κλειδιών
		cnt_key += 1
		# τέλος της while που περνάει όλα τα κλειδιά
	# επιστρέφει από την συνάρτηση
	return


# ταξινομεί αύξουσα μια λιστα 
def sort_dict(dct):
	# παίρνει τα κλειδιά του λεξικού
	dct_keys = list(dct.keys())
	# σημαία που σηματοδοτεί εάν η λίστα είναι τεξινομημένη
	sorted_flag = False
	# όσο δεν είναι ταξινομημένη η λίστα
	while(not sorted_flag):
		# θέτει τη λίστα ως ταξινομημένη
		sorted_flag = True
		# δεικτης που περνάει τη λίστα
		cnt_in = 0
		# οσο δεν έχει περάσει όλη τη λίστα
		while(cnt_in < len(dct)-1):
			# αν το τωρινό στοιχείο είναι μεγαλήτερο από το επόμενο
			if(dct[dct_keys[cnt_in]] > dct[dct_keys[cnt_in+1]]):
				# αλλάζει τις θέσεις
				dct[dct_keys[cnt_in]], dct[dct_keys[cnt_in+1]] = dct[dct_keys[cnt_in+1]], dct[dct_keys[cnt_in]]
				# κάνει τη σημαία false
				sorted_flag = False
			# αυξάνει τον δείκτη
			cnt_in += 1	
	# επιστρέφει από τη συνάρτηση
	return
