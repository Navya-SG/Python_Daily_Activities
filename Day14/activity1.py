'''invited = {"Alice","Bob","Charlie"}
arrived = {"Alice","Bob","Diana"}
unexpected = arrived - invited
if unexpected:
	print("Unexpected guests arived:",*unexpected)'''

invited = {"Alice","Bob","Charlie"}
arrived = {"Alice","Bob","Diana"}
inv = dict(zip(invited,arrived))
unexpected = (inv.keys() != inv.values())
if inv.keys() != inv.values():
	print("Unexpected guests arived:",inv.values())

