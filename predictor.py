### Custom definitions and classes if any ###
import pandas as pd

import numpy as np
df=pd.read_csv('afteraddingdatafinal2.csv')
X=df.iloc[:,:-1].values
y=df.iloc[:,-1].values
from sklearn.ensemble import RandomForestRegressor
reg = RandomForestRegressor(n_estimators=300,
                          max_depth=15,
                          min_samples_split=5,
                          min_samples_leaf=50,
                          max_features=None,
                          oob_score=True,
                          n_jobs=-1,
                          random_state=42)
reg.fit(X,y)
def predictRuns(testInput):
    data=pd.read_csv(testInput)
    aaax=[('Abdur Razzak', 0), ('Arshdeep Singh', 0), ('C Nanda', 0), ('DR Sams', 0), ('IC Pandey', 0), ('JL Denly', 0), ('KK Ahmed', 0), ('L Ablish', 0), ('M Jansen', 0), ('ND Doshi', 0), ('RR Bhatkal', 0), ('S Kaushik', 0), ('S Lamichhane', 0), ('SS Cottrell', 0), ('Sunny Gupta', 0), ('U Kaul', 0), ('V Pratap Singh', 0), ('Y Prithvi Raj', 0), ('BE Hendricks', 1), ('DJ Muthuswami', 1), ('DP Vijaykumar', 1), ('HF Gurney', 1), ('LE Plunkett', 1), ('M de Lange', 1), ('Mustafizur Rahman', 1), ('NJ Rimmington', 1), ('PM Sarvesh Kumar', 1), ('S Ladda', 1), ('SE Bond', 1), ('Shoaib Ahmed', 1), ('YA Abdulla', 1), ('H Das', 2), ('Mashrafe Mortaza', 2), ('P Parameswaran', 2), ('RG More', 2), ('RS Gavaskar', 2), ('S Randiv', 2), ('SB Wagh', 2), ('VS Yeligati', 2), ('A Singh', 3), ('BAW Mendis', 3), ('KP Appanna', 3), ('Kamran Khan', 3), ('M Prasidh Krishna', 3), ('MA Wood', 3), ('Mohammad Asif', 3), ('S Tyagi', 3), ('Shahbaz Ahmed', 3), ('Shoaib Akhtar', 3), ('T Natarajan', 3), ('Younis Khan', 3), ('A Chandila', 4), ('A Dananjaya', 4), ('A Uniyal', 4), ('AJ Turner', 4), ('Avesh Khan', 4), ('CRD Fernando', 4), ('D Kalyankrishna', 4), ('DP Nannes', 4), ('FH Edwards', 4), ('GD McGrath', 4), ('JE Taylor', 4), ('KA Jamieson', 4), ('Kartik Tyagi', 4), ('R Ninan', 4), ('RS Sodhi', 4), ('A Zampa', 5), ('B Laughlin', 5), ('B Stanlake', 5), ('Mohammad Ashraful', 5), ('P Awana', 5), ('Rasikh Salam', 5), ('SJ Srivastava', 5), ('Shivam Sharma', 5), ('VRV Singh', 5), ('BA Bhatt', 6), ('DM Bravo', 6), ('GC Viljoen', 6), ('KMDN Kulasekara', 6), ('PSP Handscomb', 6), ('SS Shaikh', 6), ('A Nortje', 7), ('AF Milne', 7), ('AN Ghosh', 7), ('I Malhotra', 7), ('Pankaj Singh', 7), ('Ravi Bishnoi', 7), ('CJ McKay', 8), ('CK Langeveldt', 8), ('J Yadav', 8), ('JPR Scantlebury-Searles', 8), ('Jaskaran Singh', 8), ('M Ashwin', 8), ('P Chopra', 8), ('P Dubey', 8), ('RK Bhui', 8), ('SB Joshi', 8), ('TM Srivastava', 8), ('Ankit Soni', 9), ('RM Patidar', 9), ('TS Mills', 9), ('UA Birla', 9), ('VS Malik', 9), ('AG Murtaza', 10), ('D du Preez', 10), ('IS Sodhi', 10), ('KAJ Roach', 10), ('X Thalaivan Sargunam', 10), ('AA Noffke', 11), ('J Theron', 11), ('SMSM Senanayake', 11), ('AA Chavan', 12), ('AR Bawne', 12), ('BB Sran', 12), ('DAJ Bracewell', 12), ('K Upadhyay', 12), ('Karanveer Singh', 12), ('M Ntini', 12), ('S Kaul', 12), ('Swapnil Singh', 12), ('T Henderson', 12), ('T Kohli', 12), ('TA Boult', 12), ('CV Varun', 13), ('DNT Zoysa', 13), ('DT Patil', 13), ('KJ Abbott', 13), ('Mujeeb Ur Rahman', 13), ('SM Harwood', 13), ('T Thushara', 13), ('F Behardien', 14), ('AS Joseph', 15), ('GR Napier', 15), ('I Udana', 15), ('JL Pattinson', 15), ('MDKJ Perera', 15), ('S Badree', 15), ('SD Lad', 15), ('TD Paine', 15), ('DR Shorey', 16), ('SA Abbott', 16), ('RD Chahar', 17), ('BJ Haddin', 18), ('Harmeet Singh', 18), ('Parvez Rasool', 18), ('CK Kapugedera', 19), ('JJ van der Wath', 19), ('P Sahu', 19), ('R Bishnoi', 19), ('R Shukla', 19), ('Vishnu Vinod', 19), ('A Mukund', 20), ('AC Thomas', 20), ('DS Lehmann', 20), ('Harpreet Singh', 20), ('NJ Maddinson', 20), ('P Ray Barman', 20), ('PV Tambe', 20), ('RR Raje', 20), ('T Banton', 20), ('Y Gnaneswara Rao', 20), ('DR Martyn', 21), ('TU Deshpande', 21), ('VY Mahesh', 21), ('C Madan', 22), ('GB Hogg', 22), ('Harpreet Brar', 22), ('KMA Paul', 22), ('M Muralitharan', 22), ('PP Ojha', 22), ('BMAJ Mendis', 23), ('KL Nagarkoti', 23), ('MS Wade', 23), ('SW Tait', 23), ('DE Bollinger', 24), ('KC Cariappa', 24), ('Shivam Mavi', 24), ('A Choudhary', 25), ('J Arunkumar', 25), ('AS Rajpoot', 27), ('JM Kemp', 27), ('MA Khote', 27), ('S Chanderpaul', 27), ('YS Chahal', 27), ('NL McCullum', 28), ('ER Dwivedi', 29), ('SB Jakati', 29), ('VH Zol', 29), ('AB Dinda', 30), ('J Syed Mohammad', 30), ('NA Saini', 30), ('M Markande', 31), ('PJ Sangwan', 31), ('T Taibu', 31), ('P Simran Singh', 32), ('D Salunkhe', 33), ('AT Carey', 34), ('Imran Tahir', 34), ('AP Dole', 35), ('MJ Santner', 35), ('N Jagadeesan', 35), ('B Sumanth', 36), ('Basil Thampi', 36), ('CJ Jordan', 36), ('Joginder Sharma', 36), ('KW Richardson', 36), ('NS Naik', 36), ('A Mithun', 37), ('L Ronchi', 37), ('RJ Peterson', 37), ('AN Ahmed', 38), ('SP Jackson', 38), ('S Narwal', 39), ('S Sriram', 39), ('Anureet Singh', 40), ('MM Patel', 40), ('Sohail Tanvir', 40), ('YBK Jaiswal', 40), ('L Balaji', 41), ('A Kumble', 42), ('AUK Pathan', 42), ('LPC Silva', 43), ('AB Barath', 44), ('BR Dunk', 44), ('JJ Bumrah', 44), ('S Sreesanth', 44), ('Sunny Singh', 44), ('Umar Gul', 44), ('LH Ferguson', 45), ('S Nadeem', 46), ('SK Trivedi', 47), ('SN Thakur', 48), ('A Nehra', 49), ('Sandeep Sharma', 49), ('Yashpal Singh', 49), ('AS Yadav', 52), ('VR Aaron', 52), ('DJ Thornely', 53), ('Mohammed Siraj', 53), ('SB Bangar', 53), ('RR Rossouw', 54), ('AG Paunikar', 56), ('R Rampaul', 56), ('J Suchith', 57), ('Shoaib Malik', 57), ('A Chopra', 58), ('I Sharma', 58), ('Kuldeep Yadav', 59), ('M Rawat', 59), ('Mohammed Shami', 59), ('RP Singh', 59), ('RV Gomez', 60), ('CR Woakes', 63), ('WA Mota', 63), ('JDS Neesham', 64), ('KB Arun Karthik', 64), ('S Aravind', 64), ('Anirudh Singh', 66), ('JD Unadkat', 66), ('H Klaasen', 68), ('RR Powar', 68), ('Mohammad Hafeez', 69), ('R Sharma', 71), ('A Flintoff', 72), ('LS Livingstone', 72), ('WD Parnell', 74), ('M Klinger', 77), ('RR Sarwan', 77), ('AA Bilakhia', 78), ('TR Birt', 79), ('B Akhil', 80), ('NM Coulter-Nile', 80), ('AD Mascarenhas', 81), ('SE Rutherford', 82), ('Shahid Afridi', 82), ('DL Chahar', 84), ('IR Jaggi', 84), ('RK Singh', 84), ('WPUJC Vaas', 84), ('JR Philippe', 86), ('LA Carseldine', 87), ('Ankit Sharma', 89), ('MK Lomror', 89), ('RE Levi', 89), ('AP Majumdar', 90), ('AD Nath', 91), ('MJ McClenaghan', 92), ('SL Malinga', 95), ('S Rana', 96), ('Iqbal Abdulla', 97), ('CJ Ferguson', 101), ('DJ Jacobs', 102), ('AJ Tye', 104), ('MJ Clarke', 104), ('PR Shah', 104), ('RT Ponting', 104), ('SD Chitnis', 104), ('MS Gony', 106), ('MA Starc', 107), ('JO Holder', 109), ('TK Curran', 109), ('JDP Oram', 110), ('LJ Wright', 110), ('DS Kulkarni', 111), ('RJ Quiney', 114), ('TG Southee', 118), ('DJ Harris', 119), ('M Kartik', 119), ('RJ Harris', 119), ('Z Khan', 121), ('KK Cooper', 122), ('DJM Short', 123), ('Misbah-ul-Haq', 124), ('AC Blizzard', 126), ('MM Sharma', 127), ('AB McDonald', 130), ('M Morkel', 130), ('Niraj Patel', 131), ('P Dogra', 131), ('BB Samantray', 132), ('Kamran Akmal', 132), ('UT Yadav', 132), ('B Lee', 133), ('Abdul Samad', 134), ('K Rabada', 134), ('UT Khawaja', 134), ('D Wiese', 136), ('MC Juneja', 138), ('HV Patel', 139), ('SB Styris', 139), ('W Jaffer', 139), ('DL Vettori', 141), ('PK Garg', 142), ('N Saini', 145), ('Sachin Baby', 145), ('AD Hales', 152), ('Rashid Khan', 153), ('SM Pollock', 154), ('Abhishek Sharma', 155), ('S Vidyut', 156), ('R Dhawan', 159), ('S Anirudha', 164), ('RE van der Merwe', 170), ('S Gopal', 170), ('PA Reddy', 172), ('R McLaren', 172), ('MN Samuels', 174), ('MN van Wyk', 175), ('Mohammad Nabi', 175), ('S Dube', 175), ('DW Steyn', 179), ('MF Maharoof', 181), ('MG Johnson', 183), ('C Munro', 185), ('DH Yagnik', 187), ('JJ Roy', 187), ('AC Voges', 190), ('Bipul Sharma', 190), ('K Gowtham', 191), ('AB Agarkar', 193), ('B Kumar', 196), ('CR Brathwaite', 198), ('CM Gautam', 199), ('AS Raut', 204), ('BJ Rohrer', 205), ('JC Archer', 205), ('FY Fazal', 207), ('YV Takawale', 207), ('SP Fleming', 209), ('SK Warne', 210), ('Salman Butt', 211), ('PD Collingwood', 213), ('Washington Sundar', 213), ('CA Ingram', 214), ('TM Head', 214), ('RD Gaikwad', 227), ('PJ Cummins', 233), ('K Goel', 234), ('MR Marsh', 234), ('AA Jhunjhunwala', 235), ('BCJ Cutting', 251), ('MD Mishra', 254), ('SM Katich', 254), ('R Parag', 259), ('MJ Guptill', 276), ('M Kaif', 280), ('SO Hetmyer', 284), ('A Ashish Reddy', 288), ('R Sathish', 288), ('B Chipli', 292), ('VVS Laxman', 296), ('MJ Lumb', 297), ('GH Vihari', 303), ('Y Nagar', 309), ('SP Goswami', 312), ('C de Grandhomme', 317), ('DJG Sammy', 317), ('DB Das', 321), ('SM Curran', 322), ('UBT Chand', 327), ('LA Pomersbach', 330), ('R Vinay Kumar', 338), ('RN ten Doeschate', 338), ('JEC Franklin', 342), ('KV Sharma', 343), ('SW Billings', 352), ('R Bhatia', 356), ('MM Ali', 360), ('P Kumar', 363), ('AP Tare', 365), ('R Tewatia', 386), ('P Negi', 392), ('S Sohal', 400), ('DB Ravi Teja', 401), ('A Mishra', 402), ('Azhar Mahmood', 409), ('AL Menaria', 416), ('MV Boucher', 416), ('CA Pujara', 421), ('J Botha', 424), ('LR Shukla', 432), ('R Ashwin', 432), ('JR Hopes', 433), ('SN Khan', 454), ('NLTC Perera', 461), ('SA Asnodkar', 462), ('E Lewis', 464), ('DT Christian', 468), ('D Padikkal', 502), ('N Pooran', 539), ('PC Valthaty', 539), ('Gurkeerat Singh', 541), ('M Manhas', 544), ('OA Shah', 550), ('JP Faulkner', 554), ('RS Bopara', 557), ('CJ Anderson', 559), ('CH Morris', 571), ('HM Amla', 600), ('PP Chawla', 620), ('JD Ryder', 630), ('DJ Hooda', 653), ('V Shankar', 691), ('GJ Bailey', 692), ('TL Suman', 701), ('AM Nayar', 722), ('AD Mathews', 765), ('GC Smith', 800), ('Shakib Al Hasan', 801), ('ST Jayasuriya', 843), ('MP Stoinis', 881), ('JM Bairstow', 888), ('Harbhajan Singh', 891), ('MS Bisla', 894), ('PP Shaw', 922), ('STR Binny', 923), ('BA Stokes', 951), ('HH Gibbs', 955), ('SP Narine', 959), ('AR Patel', 962), ('Shubman Gill', 982), ('MC Henriques', 999), ('CL White', 1000), ('JA Morkel', 1026), ('A Symonds', 1028), ('KP Pietersen', 1039), ('Y Venugopal Rao', 1051), ('KH Pandya', 1058), ('M Vohra', 1067), ('LRPL Taylor', 1084), ('RA Tripathi', 1084), ('LMP Simmons', 1127), ('KM Jadhav', 1200), ('ML Hayden', 1205), ('IK Pathan', 1250), ('TM Dilshan', 1251), ('Ishan Kishan', 1283), ('EJG Morgan', 1352), ('CA Lynn', 1384), ('DJ Hussey', 1384), ('SS Tiwary', 1460), ('SC Ganguly', 1464), ('HH Pandya', 1468), ('BJ Hodge', 1477), ('S Badrinath', 1515), ('KK Nair', 1533), ('N Rana', 1570), ('DJ Bravo', 1578), ('AD Russell', 1618), ('GJ Maxwell', 1638), ('NV Ojha', 1644), ('KS Williamson', 1673), ('Mandeep Singh', 1727), ('MK Tiwary', 1777), ('KC Sangakkara', 1780), ('MA Agarwal', 1783), ('JC Buttler', 1796), ('DPMD Jayawardene', 1929), ('DA Miller', 1958), ('Q de Kock', 2052), ('MEK Hussey', 2064), ('WP Saha', 2081), ('SA Yadav', 2128), ('JP Duminy', 2131), ('AJ Finch', 2144), ('RR Pant', 2193), ('AC Gilchrist', 2215), ('R Dravid', 2270), ('SS Iyer', 2294), ('RA Jadeja', 2315), ('F du Plessis', 2387), ('SPD Smith', 2444), ('DR Smith', 2515), ('SR Tendulkar', 2537), ('JH Kallis', 2567), ('SE Marsh', 2612), ('SV Samson', 2663), ('KL Rahul', 2747), ('M Vijay', 2749), ('Yuvraj Singh', 2884), ('V Sehwag', 2915), ('PA Patel', 3041), ('BB McCullum', 3103), ('KA Pollard', 3221), ('YK Pathan', 3385), ('MK Pandey', 3490), ('AT Rayudu', 3826), ('KD Karthik', 4022), ('SR Watson', 4042), ('AM Rahane', 4104), ('G Gambhir', 4479), ('MS Dhoni', 4855), ('RV Uthappa', 4880), ('AB de Villiers', 5083), ('CH Gayle', 5136), ('RG Sharma', 5415), ('DA Warner', 5525), ('S Dhawan', 5539), ('SK Raina', 5667), ('V Kohli', 6125)]
    aaay=[('PP Chawla', 4330), ('Harbhajan Singh', 4046), ('A Mishra', 3940), ('DJ Bravo', 3897), ('R Ashwin', 3804), ('UT Yadav', 3687), ('RA Jadeja', 3531), ('SL Malinga', 3486), ('B Kumar', 3378), ('P Kumar', 3342), ('SP Narine', 3219), ('R Vinay Kumar', 3041), ('Z Khan', 2860), ('YS Chahal', 2823), ('SR Watson', 2742), ('Sandeep Sharma', 2721), ('JJ Bumrah', 2711), ('IK Pathan', 2711), ('I Sharma', 2681), ('DW Steyn', 2583), ('A Nehra', 2537), ('AR Patel', 2502), ('MM Sharma', 2488), ('DS Kulkarni', 2465), ('JD Unadkat', 2447), ('RP Singh', 2417), ('JA Morkel', 2409), ('PP Ojha', 2399), ('JH Kallis', 2348), ('M Morkel', 2136), ('AB Dinda', 2103), ('L Balaji', 2083), ('Mohammed Shami', 2063), ('R Bhatia', 2059), ('CH Morris', 1981), ('KA Pollard', 1975), ('SK Trivedi', 1944), ('JP Faulkner', 1849), ('MJ McClenaghan', 1839), ('AD Russell', 1775), ('M Muralitharan', 1765), ('S Nadeem', 1764), ('MG Johnson', 1740), ('MM Patel', 1733), ('Imran Tahir', 1713), ('Shakib Al Hasan', 1710), ('TA Boult', 1648), ('KV Sharma', 1645), ('Rashid Khan', 1609), ('KH Pandya', 1555), ('S Kaul', 1476), ('VR Aaron', 1474), ('SB Jakati', 1474), ('SK Warne', 1465), ('YK Pathan', 1443), ('M Kartik', 1418), ('SN Thakur', 1408), ('HV Patel', 1407), ('HH Pandya', 1340), ('DL Chahar', 1322), ('MS Gony', 1317), ('TG Southee', 1316), ('MC Henriques', 1255), ('Kuldeep Yadav', 1251), ('S Sreesanth', 1221), ('PJ Sangwan', 1201), ('AB Agarkar', 1174), ('S Gopal', 1173), ('K Rabada', 1145), ('SK Raina', 1139), ('B Lee', 1126), ('Iqbal Abdulla', 1125), ('Mohammed Siraj', 1123), ('R Sharma', 1100), ('AD Mathews', 1095), ('Yuvraj Singh', 1091), ('A Kumble', 1089), ('RJ Harris', 1085), ('DT Christian', 1083), ('S Aravind', 1057), ('P Awana', 1046), ('NLTC Perera', 1031), ('JC Archer', 1008), ('BA Stokes', 993), ('PJ Cummins', 979), ('P Negi', 954), ('NM Coulter-Nile', 945), ('MP Stoinis', 900), ('DL Vettori', 894), ('AJ Tye', 892), ('PV Tambe', 866), ('M Prasidh Krishna', 855), ('RD Chahar', 851), ('JP Duminy', 847), ('AS Rajpoot', 844), ('DR Smith', 825), ('J Botha', 818), ('DP Nannes', 815), ('NA Saini', 802), ('M Ashwin', 796), ('KK Cooper', 789), ('GJ Maxwell', 786), ('BB Sran', 767), ('Washington Sundar', 765), ('STR Binny', 763), ('CH Gayle', 755), ('WD Parnell', 731), ('MA Starc', 725), ('DE Bollinger', 716), ('Harmeet Singh', 713), ('Azhar Mahmood', 707), ('Basil Thampi', 704), ('SM Curran', 697), ('A Symonds', 694), ('Mustafizur Rahman', 693), ('R Tewatia', 684), ('T Natarajan', 673), ('SW Tait', 668), ('R Dhawan', 655), ('A Singh', 639), ('Anureet Singh', 636), ('CJ Jordan', 631), ('IC Pandey', 609), ('CR Woakes', 608), ('GB Hogg', 585), ('Bipul Sharma', 581), ('KK Ahmed', 576), ('K Gowtham', 576), ('Mujeeb Ur Rahman', 568), ('JR Hopes', 562), ('R McLaren', 558), ('JO Holder', 552), ('VRV Singh', 549), ('RR Powar', 538), ('MF Maharoof', 532), ('A Nortje', 529), ('CJ Anderson', 525), ('RE van der Merwe', 515), ('AN Ahmed', 515), ('VY Mahesh', 511), ('BW Hilfenhaus', 497), ('Shivam Mavi', 487), ('DJ Hussey', 485), ('A Mithun', 477), ('Pankaj Singh', 472), ('LR Shukla', 458), ('Ankit Sharma', 453), ('KW Richardson', 450), ('RG Sharma', 449), ('SJ Srivastava', 444), ('M Markande', 435), ('LH Ferguson', 434), ('CV Varun', 430), ('BCJ Cutting', 430), ('MR Marsh', 426), ('Joginder Sharma', 421), ('AC Thomas', 416), ('D Wiese', 409), ('BA Bhatt', 408), ('A Ashish Reddy', 400), ('J Suchith', 397), ('ST Jayasuriya', 396), ('CR Brathwaite', 384), ('Ravi Bishnoi', 381), ('A Zampa', 373), ('Kartik Tyagi', 372), ('V Kohli', 371), ('SC Ganguly', 370), ('TM Dilshan', 368), ('TK Curran', 368), ('GD McGrath', 366), ('AD Mascarenhas', 365), ('WPUJC Vaas', 364), ('Mohammad Nabi', 363), ('JDP Oram', 362), ('DJG Sammy', 354), ('KC Cariappa', 349), ('MM Ali', 342), ('AA Chavan', 339), ('Y Venugopal Rao', 338), ('Arshdeep Singh', 336), ('L Ngidi', 331), ('S Badree', 329), ('DJ Hooda', 326), ('Avesh Khan', 324), ('Karanveer Singh', 323), ('C de Grandhomme', 323), ('AM Nayar', 323), ('AG Murtaza', 322), ('JL Pattinson', 321), ('R Rampaul', 319), ('JD Ryder', 314), ('YA Abdulla', 311), ('J Theron', 311), ('BJ Hodge', 310), ('SM Pollock', 307), ('Mohammad Asif', 307), ('CRD Fernando', 306), ('BAW Mendis', 306), ('S Tyagi', 304), ('S Kaushik', 304), ('RS Bopara', 301), ('V Pratap Singh', 300), ('S Lamichhane', 297), ('KP Appanna', 291), ('J Yadav', 290), ('J Syed Mohammad', 286), ('I Udana', 286), ('MN Samuels', 285), ('B Laughlin', 284), ('SB Styris', 278), ('Sohail Tanvir', 275), ('Parvez Rasool', 273), ('VS Malik', 268), ('AB McDonald', 263), ('M Ntini', 257), ('Kamran Khan', 248), ('B Akhil', 246), ('JDS Neesham', 245), ('A Chandila', 245), ('V Shankar', 243), ('P Amarnath', 241), ('KMA Paul', 239), ('HF Gurney', 239), ('BE Hendricks', 239), ('Shahid Afridi', 237), ('V Sehwag', 236), ('R Sathish', 233), ('KL Nagarkoti', 233), ('GC Viljoen', 229), ('LE Plunkett', 228), ('P Parameswaran', 226), ('SE Bond', 225), ('S Ladda', 225), ('JEC Franklin', 225), ('S Randiv', 223), ('SB Bangar', 221), ('KP Pietersen', 218), ('R Shukla', 217), ('RR Raje', 214), ('SMSM Senanayake', 211), ('PC Valthaty', 207), ('Anand Rajan', 206), ('DP Vijaykumar', 205), ('AM Salvi', 205), ('IS Sodhi', 204), ('S Narwal', 203), ('B Stanlake', 200), ('CK Langeveldt', 199), ('Umar Gul', 198), ('TL Suman', 198), ('TU Deshpande', 193), ('AF Milne', 185), ('KJ Abbott', 182), ('SS Cottrell', 177), ('Jaskaran Singh', 174), ('M de Lange', 171), ('JP Behrendorff', 168), ('JE Taylor', 167), ('Shivam Sharma', 165), ('T Thushara', 164), ('FH Edwards', 160), ('TS Mills', 157), ('K Khejroliya', 157), ('Shoaib Ahmed', 154), ('P Suyal', 154), ('P Sahu', 152), ('T Shamsi', 151), ('R Parag', 148), ('SB Wagh', 147), ('MJ Santner', 147), ('Ankit Soni', 145), ('AL Menaria', 144), ('A Choudhary', 144), ('N Rana', 143), ('Gagandeep Singh', 142), ('TP Sudhindra', 137), ('JJ van der Wath', 134), ('RV Gomez', 130), ('AA Jhunjhunwala', 130), ('Y Nagar', 125), ('LJ Wright', 125), ('KMDN Kulasekara', 122), ('S Sandeep Warrier', 120), ('DR Sams', 114), ('AP Dole', 114), ('Abhishek Sharma', 113), ('DJ Muthuswami', 108), ('A Flintoff', 106), ('PD Collingwood', 101), ('DNT Zoysa', 100), ('WA Mota', 98), ('Gurkeerat Singh', 97), ('DJ Willey', 96), ('Abdul Samad', 96), ('RN ten Doeschate', 94), ('K Goel', 94), ('K Santokie', 91), ('B Geeves', 91), ('Swapnil Singh', 90), ('JPR Scantlebury-Searles', 89), ('Harpreet Brar', 89), ('AS Joseph', 89), ('D Kalyankrishna', 88), ('Shoaib Malik', 87), ('GS Sandhu', 86), ('CL White', 86), ('O Thomas', 85), ('S Dube', 83), ('MK Tiwary', 83), ('SB Joshi', 82), ('TM Head', 81), ('K Upadhyay', 81), ('KAJ Roach', 80), ('D Salunkhe', 80), ('ND Doshi', 79), ('L Ablish', 76), ('AC Voges', 76), ('KM Asif', 75), ('SM Harwood', 74), ('S Dhawan', 72), ('P Dubey', 72), ('MJ Clarke', 72), ('JR Hazlewood', 72), ('SC Kuggeleijn', 71), ('Mohammad Hafeez', 71), ('MJ Henry', 71), ('RJ Peterson', 70), ('AJ Finch', 67), ('A Uniyal', 67), ('JW Hastings', 66), ('R Ninan', 65), ('RG More', 63), ('AUK Pathan', 63), ('SD Chitnis', 62), ('MG Neser', 62), ('VS Yeligati', 61), ('SE Rutherford', 60), ('CJ McKay', 60), ('Shahbaz Ahmed', 59), ('SR Tendulkar', 59), ('Mashrafe Mortaza', 59), ('JM Kemp', 58), ('C Nanda', 58), ('Y Prithvi Raj', 57), ('SA Abbott', 57), ('SM Boland', 56), ('P Ray Barman', 56), ('D du Preez', 56), ('Shoaib Akhtar', 54), ('MA Khote', 52), ('MA Wood', 50), ('S Sriram', 49), ('M Vijay', 49), ('CK Kapugedera', 49), ('GH Vihari', 48), ('Sunny Gupta', 47), ('A Dananjaya', 47), ('AS Raut', 45), ('SS Agarwal', 42), ('Rasikh Salam', 42), ('PM Sarvesh Kumar', 42), ('M Manhas', 42), ('T Henderson', 41), ('AA Noffke', 41), ('DJ Thornely', 40), ('BMAJ Mendis', 36), ('RR Bhatkal', 35), ('NL McCullum', 35), ('SS Sarkar', 34), ('LMP Simmons', 34), ('Harmeet Singh (2)', 34), ('CJ Dala', 34), ('Tejas Baroka', 33), ('RW Price', 33), ('MB Parmar', 33), ('DAJ Bracewell', 32), ('KS Williamson', 31), ('A Nel', 31), ('M Jansen', 30), ('S Midhun', 29), ('Abdur Razzak', 29), ('GR Napier', 28), ('DB Ravi Teja', 28), ('MK Lomror', 27), ('KA Jamieson', 27), ('Mandeep Singh', 26), ('DJ Harris', 26), ('RR Bose', 24), ('LRPL Taylor', 24), ('CJ Green', 24), ('I Malhotra', 23), ('DJM Short', 23), ('S Vidyut', 22), ('LPC Silva', 21), ('AA Kazi', 21), ('NJ Rimmington', 20), ('Monu Kumar', 20), ('FY Fazal', 20), ('B Chipli', 20), ('S Rana', 18), ('P Prasanth', 18), ('NB Singh', 18), ('F du Plessis', 16), ('C Munro', 15), ('LS Livingstone', 13), ('C Ganapathy', 13), ('RA Tripathi', 12), ('BJ Rohrer', 12), ('RA Shaikh', 11), ('AS Roy', 11), ('Sachin Baby', 8), ('SA Yadav', 8), ('RS Gavaskar', 8), ('Y Gnaneswara Rao', 7), ('SS Mundhe', 6), ('SN Khan', 6), ('LA Carseldine', 6), ('SPD Smith', 5), ('AM Rahane', 5), ('DA Warner', 2), ('AC Gilchrist', 0)]
    aaaz=['M Chinnaswamy Stadium', 'Punjab Cricket Association Stadium, Mohali',
 'Feroz Shah Kotla', 'Eden Gardens', 'Wankhede Stadium',
 'Sawai Mansingh Stadium', 'Rajiv Gandhi International Stadium',
 'MA Chidambaram Stadium', 'Dr DY Patil Sports Academy', 'Newlands',
 "St George's Park", 'Kingsmead', 'SuperSport Park', 'Buffalo Park',
 'New Wanderers Stadium', 'De Beers Diamond Oval', 'OUTsurance Oval',
 'Brabourne Stadium', 'Sardar Patel Stadium, Motera', 'Barabati Stadium',
 'Vidarbha Cricket Association Stadium, Jamtha',
 'Himachal Pradesh Cricket Association Stadium','Nehru Stadium',
 'Holkar Cricket Stadium',
 'Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium',
 'Subrata Roy Sahara Stadium',
 'Shaheed Veer Narayan Singh International Stadium',
 'JSCA International Stadium Complex', 'Sheikh Zayed Stadium'
 'Sharjah Cricket Stadium', 'Dubai International Cricket Stadium',
 'Maharashtra Cricket Association Stadium',
 'Saurashtra Cricket Association Stadium', 'Green Park',
 'Arun Jaitley Stadium']
    aaaxyz=['Kolkata Knight Riders', 'Royal Challengers Bangalore',
 'Chennai Super Kings', 'Kings XI Punjab', 'Rajasthan Royals',
 'Delhi Daredevils', 'Deccan Chargers', 'Mumbai Indians',
 'Kochi Tuskers Kerala', 'Pune Warriors', 'Sunrisers Hyderabad',
 'Rising Pune Supergiant', 'Gujarat Lions', 'Delhi Capitals']
    abcd=data['batsmen'][0].split(",")
    xyzz=0
    akk=0
    for j in abcd:
        if "Plessis" in j:
            j="F du Plessis"
        elif "Kock" in j:
            j="Q de Kock"
        for i in range(len(aaax)):
            if aaax[i][0]==j:
                xyzz+=np.log10(i)
                akk=1
        if (akk==0):
            xyzz+=np.log10(len(aaax)+1)
    data['batsmen'][0]=xyzz
    efgh=data['bowlers'][0].split(",")
    zzyx=0
    aakk=0
    for j in efgh:
        for i in range(len(aaay)):
            if aaay[i][0]==j:
                zzyx+=np.log10(i)
                aakk=1
        if (aakk==0):
            zzyx+=np.log10(len(aaay)+1)
    data['bowlers'][0]=zzyx
    
    if data['bowling_team'][0]=="Rising Pune Supergiants":
        data['bowling_team'][0]="Rising Pune Supergiant"
    if data['batting_team'][0]=="Rising Pune Supergiants":
        data['batting_team'][0]="Rising Pune Supergiant"
    if "Punjab" in data["batting_team"][0]:
        data["batting_team"][0]="Kings XI Punjab"
    if "Punjab" in data["bowling_team"][0]:
        data["bowling_team"][0]="Kings XI Punjab"
    if "Delhi" in data["bowling_team"][0]:
        data["bowling_team"][0]="Delhi Daredevils"
    if "Delhi" in data["batting_team"][0]:
        data["batting_team"][0]="Delhi Daredevils"
    att=0
    attt=0
    for i in range(len(aaaxyz)):
        if data["batting_team"][0]==aaaxyz[i]:
            data["batting_team"][0]=i
            att=1
        if data["bowling_team"][0]==aaaxyz[i]:
            data["bowling_team"][0]=i
            attt=1
    if(att==0):
        data["batting_team"][0]=len(aaaxyz)+1
    if(attt==0):
        data["bowling_team"][0]=len(aaaxyz)+1
    if data['venue'][0]=="M.Chinnaswamy Stadium":
        data['venue'][0]="M Chinnaswamy Stadium"
    elif data['venue'][0]=="Punjab Cricket Association Stadium, Mohali" or data['venue'][0]=="Punjab Cricket Association IS Bindra Stadium, Mohali" or data['venue'][0]=="Punjab Cricket Association IS Bindra Stadium":
        data['venue'][0]="Punjab Cricket Association Stadium, Mohali"
    elif data['venue'][0]=="Wankhede Stadium" or data['venue'][0]=="Wankhede Stadium, Mumbai":
        data['venue'][0]="Wankhede Stadium"
    elif data['venue'][0]=="MA Chidambaram Stadium, Chepauk" or data['venue'][0]=="MA Chidambaram Stadium, Chepauk, Chennai" or data['venue'][0]=="MA Chidambaram Stadium":
        data['venue'][0]="MA Chidambaram Stadium"
    elif data['venue'][0]=="Rajiv Gandhi International Stadium, Uppal" or data['venue'][0]=="Rajiv Gandhi International Stadium":
        data['venue'][0]="Rajiv Gandhi International Stadium"
    atat=1
    for i in range(len(aaaz)):
        if data["venue"][0]==aaaz[i]:
            data["venue"][0]=i
            atat=0
    if(atat==1):
        data["venue"][0]=35
    x=data.iloc[:].values

        
    prediction = reg.predict(x)

    ### Your Code Here ###
    return prediction
