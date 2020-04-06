# -*- coding: utf-8 -*-


# συνάρτηση που δέχεται μια λίστα και διαγράφει τις διπλοεγγραφές
def remove_duplicates(lista):
	cnt = 0
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
	# παίρνει τα αντικείμενα του λεξικού
	values = list(dct.values())
	# παίρνει τα κλειδία του λεξικού
	keys = list(dct.keys())
	# αρχικοποιεί το δείκτη
	cnt = 0
	# για κάθε αριθμό από το 0 έως το μήκος της λιστας
	for i in range(len(values)-1):
    	# αρχικοποιεί το δεικτη για να κάνει διαγραφές 
		cnt = i+1
		# οσο υπάρχουν αντικείμενα που δεν έχουν ελεγχθεί για διπλοεγγραφές
		while(cnt < len(values)):
			# αν υπάρχει διπλοεγγραφή	
			if(values[i] == values[cnt]):
				# διαγραφει τη διπλοεγγραφή από το λεξικό
				del dct[keys[cnt]]
				# διαγράφει τη διπλοεγγραφή από τα αντικείμενα
				del values[cnt]
				# διαγράφει τη διπλοεγγραφή από τα κλειδιά				
				del keys[cnt]
				# μειώνει κατά 1 το δείκτη για να δείχνει το επόμενο γράμμα
				# εφόσον το τωρινό διαγράφεται
				cnt -= 1
			# τελος if
			# αυξάνει τον δείκτη
			cnt += 1
		# τελος while
	# τέλος for
	return
# τέλος της συνάρτησης remove_duplicates_dict


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


a_list = [10, 12, 14, 14, 16, 28, 28, 30]
remove_duplicates(a_list)
sort_list(a_list)
print(a_list)
a_dict = {"a":10, "b":12, "c":14, "d":14, "e":16, "f":28, "g":28, "h":30}
remove_duplicates_dict(a_dict)
sort_dict(a_dict)
print(a_dict)
