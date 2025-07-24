#
a={"alice","bob","clarie"}
b={"dane","eve","bob"}
c={"eli","dane","charles"}
em_ph = (a&b)-c
blo = c-(a|b)
print(f"invited by email and phone :{em_ph}, only in bloced:{blo}")

#
a={"alice","bob","clarie","charles"}
b={"dane","eve","bob","charles"}
c={"eli","dane","charles"}
print((a&b-c)|c-(a|b))