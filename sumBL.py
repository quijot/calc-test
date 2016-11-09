#!/usr/bin/env python
# 
# Autor: Santiago Pestarini <santiagonob@gmail.com>
# Basado en los datos calculados por Gustavo Noguera como 
#   corrección fija para ir de 2011.325 a 2006.632 (POSGAR2007)

"""
 Access from Python console:
   >>> import sumBL

   and then
   sumBL[<int lon_degrees>][<int lat_degrees>]['e']
   returns a float that represents Long correction in m
   >>> sumBL.disp[-61][-33]['e']

   or 'n' instead of 'e' to Lat correction

   or o dump it to a json file:
   >>> import json, sumBL
   >>> f = open('sumBL.json', 'w')
   >>> json.dump(sumBL.disp, f, indent=2)
   >>> f.close()
"""
 
disp = {
-73 : { -53 : {'e': 0.227830868, 'n': 0.003818766 },
    -52 : {'e': 0.235763875, 'n': 0.005425072 },
    -51 : {'e': 0.243899985, 'n': 0.007552272 },
    -50 : {'e': 0.252877616, 'n': 0.009502221 },
    -49 : {'e': 0.261979636, 'n': 0.012009099 },
    -48 : {'e': 0.271326017, 'n': 0.015563444 },
    -47 : {'e': 0.295262151, 'n': 0.014328122 },
    -46 : {'e': 0.319864226, 'n': 0.019596794 },
    -45 : {'e': 0.350748516, 'n': 0.02500359 },
    -44 : {'e': 0.415945093, 'n': 0.037224361 },
    -43 : {'e': 0.564486631, 'n': 0.064500561 },
    -42 : {'e': 0.837757144, 'n': 0.110178292 },
    -41 : {'e': 1.190976344, 'n': 0.176241952 },
    -40 : {'e': 1.596057443, 'n': 0.246217048 },
    -39 : {'e': 2.047318323, 'n': 0.34076718 },
    -38 : {'e': 2.525890761, 'n': 0.439571032 },
    -37 : {'e': 3.016148469, 'n': 0.542858082 },
    -36 : {'e': 2.588260162, 'n': 0.474864328 },
    -35 : {'e': 2.059697121, 'n': 0.38778157 }},
-72 : { -54 : {'e': 0.159573804, 'n': -0.011751623 },
    -53 : {'e': 0.162083166, 'n': -0.011238567 },
    -52 : {'e': 0.167277203, 'n': -0.011002278 },
    -51 : {'e': 0.169222064, 'n': -0.009823664 },
    -50 : {'e': 0.170212932, 'n': -0.009182647 },
    -49 : {'e': 0.17070572, 'n': -0.009497255 },
    -48 : {'e': 0.170258865, 'n': -0.010125327 },
    -47 : {'e': 0.174779802, 'n': -0.013794432 },
    -46 : {'e': 0.178674591, 'n': -0.012502649 },
    -45 : {'e': 0.168233239, 'n': -0.012311255 },
    -44 : {'e': 0.167848165, 'n': -0.013665084 },
    -43 : {'e': 0.24200787, 'n': -0.000860945 },
    -42 : {'e': 0.54933787, 'n': 0.051854431 },
    -41 : {'e': 0.928298138, 'n': 0.117408336 },
    -40 : {'e': 1.333152104, 'n': 0.190416831 },
    -39 : {'e': 1.742266672, 'n': 0.278838221 },
    -38 : {'e': 2.123655932, 'n': 0.365268095 },
    -37 : {'e': 2.317541338, 'n': 0.417110683 },
    -36 : {'e': 2.1058369, 'n': 0.388493569 },
    -35 : {'e': 1.652224455, 'n': 0.307706778 },
    -34 : {'e': 1.196136965, 'n': 0.235515574 },
    -33 : {'e': 0.821613916, 'n': 0.168922437 },
    -32 : {'e': 0.623989959, 'n': 0.124348313 },
    -31 : {'e': 0.510815275, 'n': 0.093531392 },
    -30 : {'e': 0.455417083, 'n': 0.069918224 },
    -29 : {'e': 0.400043491, 'n': 0.050509223 },
    -28 : {'e': 0.351870413, 'n': 0.037141107 }},
-71 : { -54 : {'e': 0.103445255, 'n': -0.026159359 },
    -53 : {'e': 0.101900445, 'n': -0.027619575 },
    -52 : {'e': 0.106830495, 'n': -0.026764866 },
    -51 : {'e': 0.102744571, 'n': -0.025200769 },
    -50 : {'e': 0.097375331, 'n': -0.025143713 },
    -49 : {'e': 0.092383762, 'n': -0.028106933 },
    -48 : {'e': 0.082467637, 'n': -0.031164159 },
    -47 : {'e': 0.06662755, 'n': -0.032774513 },
    -46 : {'e': 0.061244559, 'n': -0.040979148 },
    -45 : {'e': 0.032256992, 'n': -0.045601731 },
    -44 : {'e': -0.003351315, 'n': -0.05388048 },
    -43 : {'e': 0.001029586, 'n': -0.056384858 },
    -42 : {'e': 0.304527541, 'n': -0.007727008 },
    -41 : {'e': 0.663641278, 'n': 0.060064518 },
    -40 : {'e': 0.997192575, 'n': 0.121111167 },
    -39 : {'e': 1.320529393, 'n': 0.194974736 },
    -38 : {'e': 1.573007351, 'n': 0.256004233 },
    -37 : {'e': 1.661811257, 'n': 0.285321561 },
    -36 : {'e': 1.524225693, 'n': 0.27185833 },
    -35 : {'e': 1.173681072, 'n': 0.215877099 },
    -34 : {'e': 0.744187895, 'n': 0.154544926 },
    -33 : {'e': 0.343717927, 'n': 0.093775772 },
    -32 : {'e': 0.282106591, 'n': 0.05630829 },
    -31 : {'e': 0.265356787, 'n': 0.036898497 },
    -30 : {'e': 0.260958973, 'n': 0.023551606 },
    -29 : {'e': 0.237062641, 'n': 0.014182299 },
    -28 : {'e': 0.208799274, 'n': 0.000783368 },
    -27 : {'e': 0.185796599, 'n': -0.006180647 },
    -26 : {'e': 0.15625205, 'n': -0.010000605 },
    -25 : {'e': 0.131040801, 'n': -0.017223418 },
    -24 : {'e': 0.103978857, 'n': -0.031250618 },
    -23 : {'e': 0.059889854, 'n': -0.044458366 },
    -22 : {'e': 0.009586989, 'n': -0.053859877 },
    -21 : {'e': -0.027571965, 'n': -0.0640328 },
    -20 : {'e': -0.042066829, 'n': -0.0677724 }},
-70 : { -55 : {'e': 0.045103786, 'n': -0.035470641 },
    -54 : {'e': 0.047641337, 'n': -0.036808761 },
    -53 : {'e': 0.0520985, 'n': -0.037478589 },
    -52 : {'e': 0.051345701, 'n': -0.040140779 },
    -51 : {'e': 0.04752415, 'n': -0.038532949 },
    -50 : {'e': 0.040403265, 'n': -0.040312647 },
    -49 : {'e': 0.030191382, 'n': -0.043902519 },
    -48 : {'e': 0.017247635, 'n': -0.047748371 },
    -47 : {'e': 0.003358929, 'n': -0.053377767 },
    -46 : {'e': -0.012423476, 'n': -0.060853323 },
    -45 : {'e': -0.037528921, 'n': -0.067390396 },
    -44 : {'e': -0.051410602, 'n': -0.072864324 },
    -43 : {'e': 0.000887059, 'n': -0.069272596 },
    -42 : {'e': 0.176456516, 'n': -0.044871108 },
    -41 : {'e': 0.421706912, 'n': -0.007675682 },
    -40 : {'e': 0.652634192, 'n': 0.037024389 },
    -39 : {'e': 0.87489069, 'n': 0.093106835 },
    -38 : {'e': 1.049672435, 'n': 0.137285002 },
    -37 : {'e': 1.117305277, 'n': 0.168603064 },
    -36 : {'e': 1.035134011, 'n': 0.16763255 },
    -35 : {'e': 0.793824922, 'n': 0.129822023 },
    -34 : {'e': 0.441480308, 'n': 0.083833101 },
    -33 : {'e': 0.142153241, 'n': 0.035964348 },
    -32 : {'e': 0.065857627, 'n': -0.007189206 },
    -31 : {'e': 0.078235594, 'n': -0.017056085 },
    -30 : {'e': 0.100346594, 'n': -0.017408579 },
    -29 : {'e': 0.110479931, 'n': -0.014891162 },
    -28 : {'e': 0.109768611, 'n': -0.018943597 },
    -27 : {'e': 0.102008645, 'n': -0.023252565 },
    -26 : {'e': 0.088765822, 'n': -0.031525716 },
    -25 : {'e': 0.060261401, 'n': -0.039777167 },
    -24 : {'e': 0.031400978, 'n': -0.047182975 },
    -23 : {'e': -0.008818692, 'n': -0.051208259 },
    -22 : {'e': -0.055129467, 'n': -0.07326548 },
    -21 : {'e': -0.097996193, 'n': -0.088532341 },
    -20 : {'e': -0.098080254, 'n': -0.079233868 }},
-69 : { -55 : {'e': -0.010635462, 'n': -0.045016254 },
    -54 : {'e': 0.002880667, 'n': -0.045424928 },
    -53 : {'e': 0.012627674, 'n': -0.047958681 },
    -52 : {'e': 0.00840854, 'n': -0.047097409 },
    -51 : {'e': 0.003056556, 'n': -0.049616017 },
    -50 : {'e': -0.005194972, 'n': -0.052454537 },
    -49 : {'e': -0.01513809, 'n': -0.056034314 },
    -48 : {'e': -0.027662971, 'n': -0.060102475 },
    -47 : {'e': -0.036368647, 'n': -0.067104279 },
    -46 : {'e': -0.043442799, 'n': -0.073499902 },
    -45 : {'e': -0.063036636, 'n': -0.079698809 },
    -44 : {'e': -0.060969556, 'n': -0.082503398 },
    -43 : {'e': -0.015222923, 'n': -0.081565179 },
    -42 : {'e': 0.087438233, 'n': -0.072802069 },
    -41 : {'e': 0.220190283, 'n': -0.059247554 },
    -40 : {'e': 0.344969924, 'n': -0.047230327 },
    -39 : {'e': 0.466813837, 'n': -0.02820057 },
    -38 : {'e': 0.610768796, 'n': 0.026206453 },
    -37 : {'e': 0.690819374, 'n': 0.065655175 },
    -36 : {'e': 0.651601112, 'n': 0.077760652 },
    -35 : {'e': 0.509249734, 'n': 0.065036007 },
    -34 : {'e': 0.292370368, 'n': 0.034162165 },
    -33 : {'e': 0.106914734, 'n': 0.001340939 },
    -32 : {'e': -0.006003029, 'n': -0.039674876 },
    -31 : {'e': -0.006319926, 'n': -0.043509341 },
    -30 : {'e': 0.022673435, 'n': -0.03846805 },
    -29 : {'e': 0.038838227, 'n': -0.036490357 },
    -28 : {'e': 0.042491358, 'n': -0.037305501 },
    -27 : {'e': 0.047759755, 'n': -0.043854054 },
    -26 : {'e': 0.037359131, 'n': -0.044651606 },
    -25 : {'e': 0.033027558, 'n': -0.040544563 },
    -24 : {'e': -0.001654955, 'n': -0.049179815 },
    -23 : {'e': -0.040250894, 'n': -0.062051451 },
    -22 : {'e': -0.069465919, 'n': -0.073517596 },
    -21 : {'e': -0.093805736, 'n': -0.082356092 },
    -20 : {'e': -0.116874934, 'n': -0.090882328 }},
-68 : { -55 : {'e': -0.050438579, 'n': -0.050996909 },
    -54 : {'e': -0.024746946, 'n': -0.052505594 },
    -53 : {'e': -0.018240035, 'n': -0.054248758 },
    -52 : {'e': -0.02338704, 'n': -0.05579044 },
    -50 : {'e': -0.038263459, 'n': -0.062018608 },
    -49 : {'e': -0.046623929, 'n': -0.06542335 },
    -48 : {'e': -0.054045461, 'n': -0.070060764 },
    -47 : {'e': -0.057584412, 'n': -0.076213752 },
    -46 : {'e': -0.058230469, 'n': -0.079597324 },
    -45 : {'e': -0.066342324, 'n': -0.083270982 },
    -44 : {'e': -0.059237173, 'n': -0.086333026 },
    -43 : {'e': -0.027502069, 'n': -0.088627592 },
    -42 : {'e': 0.026038391, 'n': -0.090553874 },
    -41 : {'e': 0.084224099, 'n': -0.09312825 },
    -40 : {'e': 0.123383931, 'n': -0.10137901 },
    -39 : {'e': 0.114548514, 'n': -0.119754142 },
    -38 : {'e': 0.291361926, 'n': -0.053302263 },
    -37 : {'e': 0.390912879, 'n': -0.005752399 },
    -36 : {'e': 0.394108895, 'n': 0.015356698 },
    -35 : {'e': 0.314992908, 'n': 0.01625078 },
    -34 : {'e': 0.191830193, 'n': 0.005494994 },
    -33 : {'e': 0.079715417, 'n': -0.012763335 },
    -32 : {'e': 0.00767634, 'n': -0.034646465 },
    -31 : {'e': -0.016958223, 'n': -0.044675532 },
    -30 : {'e': -0.004427021, 'n': -0.043683342 },
    -29 : {'e': 0.001412068, 'n': -0.042858943 },
    -28 : {'e': 0.007032509, 'n': -0.045118743 },
    -27 : {'e': 0.004038455, 'n': -0.05383792 },
    -26 : {'e': 0.003413171, 'n': -0.055108382 },
    -25 : {'e': 0.004503194, 'n': -0.056184645 },
    -24 : {'e': -0.009980943, 'n': -0.060789949 },
    -23 : {'e': -0.049601108, 'n': -0.068793036 },
    -22 : {'e': -0.074968453, 'n': -0.076667211 },
    -21 : {'e': -0.089255525, 'n': -0.077683595 },
    -20 : {'e': -0.09939947, 'n': -0.088695138 }},
-67 : { -55 : {'e': -0.064718837, 'n': -0.053262959 },
    -54 : {'e': -0.04651913, 'n': -0.055927203 },
    -53 : {'e': -0.044802677, 'n': -0.059211347 },
    -49 : {'e': -0.067027145, 'n': -0.071894672 },
    -48 : {'e': -0.06897548, 'n': -0.075335731 },
    -47 : {'e': -0.069711581, 'n': -0.079163434 },
    -46 : {'e': -0.06756274, 'n': -0.081454625 },
    -45 : {'e': -0.062533274, 'n': -0.082773459 },
    -44 : {'e': -0.04726884, 'n': -0.084618021 },
    -43 : {'e': -0.026136252, 'n': -0.088858162 },
    -42 : {'e': -0.003011072, 'n': -0.09509885 },
    -41 : {'e': 0.017660913, 'n': -0.103839206 },
    -40 : {'e': 0.033221738, 'n': -0.112127248 },
    -39 : {'e': 0.062549654, 'n': -0.10948868 },
    -38 : {'e': 0.143073783, 'n': -0.079124055 },
    -37 : {'e': 0.216665502, 'n': -0.044275325 },
    -36 : {'e': 0.232475984, 'n': -0.022459231 },
    -35 : {'e': 0.191352614, 'n': -0.014544705 },
    -34 : {'e': 0.129818776, 'n': -0.013617292 },
    -33 : {'e': 0.07147298, 'n': -0.01693752 },
    -32 : {'e': 0.019656164, 'n': -0.033187962 },
    -31 : {'e': -0.006892942, 'n': -0.040176755 },
    -30 : {'e': -0.017486645, 'n': -0.048702272 },
    -29 : {'e': -0.016078393, 'n': -0.050578324 },
    -28 : {'e': -0.009182449, 'n': -0.050033134 },
    -27 : {'e': -0.009529847, 'n': -0.052918552 },
    -26 : {'e': -0.012819279, 'n': -0.058390429 },
    -25 : {'e': -0.013586362, 'n': -0.061114632 },
    -24 : {'e': -0.02744255, 'n': -0.064947425 },
    -23 : {'e': -0.052347994, 'n': -0.070937616 },
    -22 : {'e': -0.073682855, 'n': -0.075838118 },
    -21 : {'e': -0.08246392, 'n': -0.083180743 },
    -20 : {'e': -0.079474491, 'n': -0.091796351 }},
-66 : { -55 : {'e': -0.074956131, 'n': -0.058554384 },
    -54 : {'e': -0.070602882, 'n': -0.060992965 },
    -49 : {'e': -0.078276214, 'n': -0.075524196 },
    -48 : {'e': -0.074293288, 'n': -0.077518945 },
    -47 : {'e': -0.070705973, 'n': -0.079280284 },
    -46 : {'e': -0.066260113, 'n': -0.080716457 },
    -45 : {'e': -0.050445474, 'n': -0.079866992 },
    -44 : {'e': -0.025999345, 'n': -0.078611205 },
    -43 : {'e': -0.006467308, 'n': -0.081576043 },
    -42 : {'e': -0.004936194, 'n': -0.090695977 },
    -41 : {'e': -0.001785301, 'n': -0.099407839 },
    -40 : {'e': 0.011844188, 'n': -0.103164291 },
    -39 : {'e': 0.041929167, 'n': -0.095569549 },
    -38 : {'e': 0.09044776, 'n': -0.076476301 },
    -37 : {'e': 0.126365164, 'n': -0.059385518 },
    -36 : {'e': 0.136038058, 'n': -0.044171086 },
    -35 : {'e': 0.119013174, 'n': -0.034568978 },
    -34 : {'e': 0.090423491, 'n': -0.029080311 },
    -33 : {'e': 0.060070557, 'n': -0.029792945 },
    -32 : {'e': 0.025547526, 'n': -0.032695831 },
    -31 : {'e': 0.001881186, 'n': -0.042122953 },
    -30 : {'e': -0.011015044, 'n': -0.048255026 },
    -29 : {'e': -0.01512245, 'n': -0.053318779 },
    -28 : {'e': -0.014572734, 'n': -0.055138985 },
    -27 : {'e': -0.014899884, 'n': -0.055351523 },
    -26 : {'e': -0.016298889, 'n': -0.059048166 },
    -25 : {'e': -0.016032024, 'n': -0.060618795 },
    -24 : {'e': -0.029948189, 'n': -0.065083663 },
    -23 : {'e': -0.051727393, 'n': -0.069681819 },
    -22 : {'e': -0.066175363, 'n': -0.074630885 },
    -21 : {'e': -0.073100524, 'n': -0.081772788 },
    -20 : {'e': -0.072411548, 'n': -0.087932282 }},
-65 : { -55 : {'e': -0.08848481, 'n': -0.0627721 },
    -48 : {'e': -0.081628491, 'n': -0.079851226 },
    -47 : {'e': -0.073311847, 'n': -0.080146923 },
    -46 : {'e': -0.062043745, 'n': -0.07930512 },
    -45 : {'e': -0.042012998, 'n': -0.076780577 },
    -44 : {'e': -0.009651233, 'n': -0.071968056 },
    -43 : {'e': 0.01582606, 'n': -0.071068014 },
    -42 : {'e': 0.001829591, 'n': -0.082819794 },
    -41 : {'e': 0.002845032, 'n': -0.088983853 },
    -40 : {'e': 0.012167132, 'n': -0.090440233 },
    -39 : {'e': 0.034462894, 'n': -0.084727568 },
    -38 : {'e': 0.06683452, 'n': -0.071768504 },
    -37 : {'e': 0.083152156, 'n': -0.062659923 },
    -36 : {'e': 0.087363582, 'n': -0.054519675 },
    -35 : {'e': 0.074882023, 'n': -0.051571982 },
    -34 : {'e': 0.064699086, 'n': -0.042151859 },
    -33 : {'e': 0.045658508, 'n': -0.038420114 },
    -32 : {'e': 0.02876738, 'n': -0.039712929 },
    -31 : {'e': 0.013413755, 'n': -0.04110222 },
    -30 : {'e': 0.000817946, 'n': -0.047771059 },
    -29 : {'e': -0.007676181, 'n': -0.055696361 },
    -28 : {'e': -0.003326751, 'n': -0.052060846 },
    -27 : {'e': -0.010608137, 'n': -0.052898159 },
    -26 : {'e': -0.016497601, 'n': -0.061678107 },
    -25 : {'e': -0.017782255, 'n': -0.064830703 },
    -24 : {'e': -0.030473271, 'n': -0.066467566 },
    -23 : {'e': -0.048178751, 'n': -0.068883819 },
    -22 : {'e': -0.058351923, 'n': -0.070807701 },
    -21 : {'e': -0.06370434, 'n': -0.076042548 },
    -20 : {'e': -0.068091795, 'n': -0.081614048 }},
-64 : { -44 : {'e': -0.018612915, 'n': -0.073036429 },
    -43 : {'e': -0.00396685, 'n': -0.073592773 },
    -42 : {'e': -0.000903822, 'n': -0.078520367 },
    -41 : {'e': 0.003770996, 'n': -0.081837909 },
    -40 : {'e': 0.013907999, 'n': -0.081978039 },
    -39 : {'e': 0.031830411, 'n': -0.076574501 },
    -38 : {'e': 0.049549199, 'n': -0.068918246 },
    -37 : {'e': 0.060993086, 'n': -0.061934651 },
    -36 : {'e': 0.061986909, 'n': -0.056435866 },
    -35 : {'e': 0.054581108, 'n': -0.051120937 },
    -34 : {'e': 0.045870163, 'n': -0.046092474 },
    -33 : {'e': 0.035602291, 'n': -0.042375731 },
    -32 : {'e': 0.026804819, 'n': -0.041256218 },
    -31 : {'e': 0.017774043, 'n': -0.04176276 },
    -30 : {'e': 0.012973234, 'n': -0.039810054 },
    -29 : {'e': -0.001282614, 'n': -0.049379657 },
    -28 : {'e': -0.01388389, 'n': -0.05677355 },
    -27 : {'e': -0.012510546, 'n': -0.058230272 },
    -26 : {'e': -0.018855054, 'n': -0.06458677 },
    -25 : {'e': -0.026265582, 'n': -0.072715825 },
    -24 : {'e': -0.033461813, 'n': -0.069244394 },
    -23 : {'e': -0.042790003, 'n': -0.069068273 },
    -22 : {'e': -0.047566909, 'n': -0.06947644 },
    -21 : {'e': -0.052566469, 'n': -0.071605731 },
    -20 : {'e': -0.059695027, 'n': -0.075304936 }},
-63 : { -43 : {'e': -0.015322699, 'n': -0.074512267 },
    -42 : {'e': -0.003910586, 'n': -0.07537629 },
    -41 : {'e': 0.004921555, 'n': -0.076064234 },
    -40 : {'e': 0.018038391, 'n': -0.073194932 },
    -39 : {'e': 0.034673558, 'n': -0.068533385 },
    -38 : {'e': 0.042999289, 'n': -0.063022594 },
    -37 : {'e': 0.046130064, 'n': -0.059220632 },
    -36 : {'e': 0.046884968, 'n': -0.056275598 },
    -35 : {'e': 0.04265045, 'n': -0.052090489 },
    -34 : {'e': 0.037289336, 'n': -0.048350609 },
    -33 : {'e': 0.029642269, 'n': -0.045866279 },
    -32 : {'e': 0.022541757, 'n': -0.044615103 },
    -31 : {'e': 0.015146239, 'n': -0.044853173 },
    -30 : {'e': 0.010363047, 'n': -0.044364118 },
    -29 : {'e': 0.000742944, 'n': -0.049450732 },
    -28 : {'e': -0.008384185, 'n': -0.05430954 },
    -27 : {'e': -0.013399906, 'n': -0.057397719 },
    -26 : {'e': -0.019217012, 'n': -0.062165207 },
    -25 : {'e': -0.026838129, 'n': -0.064591172 },
    -24 : {'e': -0.032668879, 'n': -0.068310384 },
    -23 : {'e': -0.037363418, 'n': -0.069074337 },
    -22 : {'e': -0.03710627, 'n': -0.069439131 },
    -21 : {'e': -0.041954156, 'n': -0.071297534 },
    -20 : {'e': -0.048433231, 'n': -0.07283065 }},
-62 : { -43 : {'e': -0.024160393, 'n': -0.074545931 },
    -42 : {'e': -0.010134168, 'n': -0.07352427 },
    -41 : {'e': 0.002551428, 'n': -0.071450888 },
    -40 : {'e': 0.016516558, 'n': -0.06829274 },
    -39 : {'e': 0.03488392, 'n': -0.062304515 },
    -38 : {'e': 0.031391297, 'n': -0.055131123 },
    -37 : {'e': 0.037763511, 'n': -0.055931307 },
    -36 : {'e': 0.038288219, 'n': -0.054634766 },
    -35 : {'e': 0.036248449, 'n': -0.052148122 },
    -34 : {'e': 0.032774012, 'n': -0.049642797 },
    -33 : {'e': 0.028158868, 'n': -0.047025553 },
    -32 : {'e': 0.021334566, 'n': -0.047644895 },
    -31 : {'e': 0.014213953, 'n': -0.047749058 },
    -30 : {'e': 0.007930895, 'n': -0.048925681 },
    -29 : {'e': 0.001154973, 'n': -0.050882674 },
    -28 : {'e': -0.006189869, 'n': -0.053321448 },
    -27 : {'e': -0.011526273, 'n': -0.056267826 },
    -26 : {'e': -0.017698881, 'n': -0.060392581 },
    -25 : {'e': -0.023506725, 'n': -0.063862054 },
    -24 : {'e': -0.02875644, 'n': -0.066549451 },
    -23 : {'e': -0.031808067, 'n': -0.068673206 },
    -22 : {'e': -0.031609467, 'n': -0.070447666 },
    -21 : {'e': -0.034586465, 'n': -0.07039005 },
    -20 : {'e': -0.039156687, 'n': -0.07218609 }},
-61 : { -42 : {'e': -0.017006678, 'n': -0.072397232 },
    -41 : {'e': -0.003325519, 'n': -0.069426399 },
    -40 : {'e': 0.010521372, 'n': -0.065433225 },
    -39 : {'e': 0.022184398, 'n': -0.06005192 },
    -38 : {'e': 0.026018526, 'n': -0.056411272 },
    -37 : {'e': 0.031838061, 'n': -0.056058184 },
    -36 : {'e': 0.033180632, 'n': -0.054133985 },
    -35 : {'e': 0.033335978, 'n': -0.05156642 },
    -34 : {'e': 0.031107942, 'n': -0.050403969 },
    -33 : {'e': 0.028602032, 'n': -0.049702033 },
    -32 : {'e': 0.021532938, 'n': -0.0485991 },
    -31 : {'e': 0.014340113, 'n': -0.04989127 },
    -30 : {'e': 0.008078028, 'n': -0.05081314 },
    -29 : {'e': 0.001629554, 'n': -0.052489734 },
    -28 : {'e': -0.003730118, 'n': -0.054389904 },
    -27 : {'e': -0.008709782, 'n': -0.057115332 },
    -26 : {'e': -0.013618555, 'n': -0.059580144 },
    -25 : {'e': -0.018606368, 'n': -0.062385947 },
    -24 : {'e': -0.022997389, 'n': -0.065094504 },
    -23 : {'e': -0.026251263, 'n': -0.067949308 },
    -22 : {'e': -0.028314348, 'n': -0.069826483 },
    -21 : {'e': -0.030438108, 'n': -0.07064072 },
    -20 : {'e': -0.032916763, 'n': -0.071356492 }},
-60 : { -40 : {'e': 0.003461793, 'n': -0.064715762 },
    -39 : {'e': 0.014690212, 'n': -0.060612632 },
    -38 : {'e': 0.022803755, 'n': -0.056557035 },
    -37 : {'e': 0.02829092, 'n': -0.054848345 },
    -36 : {'e': 0.030364449, 'n': -0.053399496 },
    -35 : {'e': 0.030503174, 'n': -0.052325619 },
    -34 : {'e': 0.029145878, 'n': -0.051540634 },
    -33 : {'e': 0.026628261, 'n': -0.050688927 },
    -32 : {'e': 0.020748756, 'n': -0.050320917 },
    -31 : {'e': 0.014845633, 'n': -0.050881679 },
    -30 : {'e': 0.006644242, 'n': -0.054718297 },
    -29 : {'e': 0.003164077, 'n': -0.053783346 },
    -28 : {'e': -0.002511075, 'n': -0.055802801 },
    -27 : {'e': -0.00510563, 'n': -0.056910422 },
    -26 : {'e': -0.009935095, 'n': -0.060459785 },
    -25 : {'e': -0.01296933, 'n': -0.06193862 },
    -24 : {'e': -0.017605093, 'n': -0.065044412 },
    -23 : {'e': -0.020638017, 'n': -0.066621973 },
    -22 : {'e': -0.022883017, 'n': -0.068649479 },
    -21 : {'e': -0.025443327, 'n': -0.069689648 },
    -20 : {'e': -0.027707337, 'n': -0.070374612 }},
-59 : { -39 : {'e': 0.009892726, 'n': -0.061081071 },
    -38 : {'e': 0.020305085, 'n': -0.056967189 },
    -37 : {'e': 0.02536842, 'n': -0.055403293 },
    -36 : {'e': 0.028078784, 'n': -0.053597871 },
    -35 : {'e': 0.028094598, 'n': -0.052799971 },
    -34 : {'e': 0.026827083, 'n': -0.052106347 },
    -33 : {'e': 0.023623119, 'n': -0.050933733 },
    -32 : {'e': 0.019270315, 'n': -0.050789274 },
    -31 : {'e': 0.014476507, 'n': -0.051514075 },
    -30 : {'e': 0.009383638, 'n': -0.051774057 },
    -29 : {'e': 0.004323036, 'n': -0.054428241 },
    -28 : {'e': 0.001011835, 'n': -0.055894619 },
    -27 : {'e': -0.002058793, 'n': -0.058119583 },
    -26 : {'e': -0.004985672, 'n': -0.05967455 },
    -25 : {'e': -0.008091267, 'n': -0.061895458 },
    -24 : {'e': -0.011312427, 'n': -0.063373442 },
    -23 : {'e': -0.014255802, 'n': -0.065080297 },
    -22 : {'e': -0.017205191, 'n': -0.067296358 },
    -21 : {'e': -0.019703684, 'n': -0.068252033 },
    -20 : {'e': -0.021221218, 'n': -0.069269474 }},
-58 : { -39 : {'e': 0.00525872, 'n': -0.062248402 },
    -38 : {'e': 0.018557085, 'n': -0.059834305 },
    -37 : {'e': 0.022777609, 'n': -0.05660663 },
    -36 : {'e': 0.025349182, 'n': -0.053410362 },
    -35 : {'e': 0.026577994, 'n': -0.051982217 },
    -34 : {'e': 0.024861864, 'n': -0.05182806 },
    -33 : {'e': 0.022185962, 'n': -0.051680349 },
    -32 : {'e': 0.018097253, 'n': -0.05172655 },
    -31 : {'e': 0.014097421, 'n': -0.052445456 },
    -30 : {'e': 0.009027923, 'n': -0.056063454 },
    -29 : {'e': 0.005949443, 'n': -0.054487702 },
    -28 : {'e': 0.003500382, 'n': -0.056796055 },
    -27 : {'e': 0.001117322, 'n': -0.058766503 },
    -26 : {'e': -0.001264691, 'n': -0.060366725 },
    -25 : {'e': -0.003776145, 'n': -0.062306675 },
    -24 : {'e': -0.006615784, 'n': -0.063548455 },
    -23 : {'e': -0.00879868, 'n': -0.064731285 },
    -22 : {'e': -0.010460774, 'n': -0.065798718 },
    -21 : {'e': -0.012678385, 'n': -0.067039365 },
    -20 : {'e': -0.014278901, 'n': -0.06841013 }},
-57 : { -39 : {'e': -0.001386362, 'n': -0.063568154 },
    -38 : {'e': 0.009667616, 'n': -0.061269134 },
    -37 : {'e': 0.01686826, 'n': -0.057292943 },
    -36 : {'e': 0.021667501, 'n': -0.054023621 },
    -35 : {'e': 0.025165119, 'n': -0.051432576 },
    -34 : {'e': 0.024078884, 'n': -0.051149513 },
    -33 : {'e': 0.021288963, 'n': -0.051329938 },
    -32 : {'e': 0.018229483, 'n': -0.05190119 },
    -31 : {'e': 0.014363341, 'n': -0.05307884 },
    -30 : {'e': 0.011208993, 'n': -0.054344733 },
    -29 : {'e': 0.008420797, 'n': -0.055768552 },
    -28 : {'e': 0.006365622, 'n': -0.057574594 },
    -27 : {'e': 0.004762992, 'n': -0.059271636 },
    -26 : {'e': 0.002410539, 'n': -0.060863361 },
    -25 : {'e': 0.000431901, 'n': -0.062183603 },
    -24 : {'e': -0.001620719, 'n': -0.06321069 },
    -23 : {'e': -0.002910781, 'n': -0.063895805 },
    -22 : {'e': -0.003903435, 'n': -0.06521127 },
    -21 : {'e': -0.005243487, 'n': -0.066074075 },
    -20 : {'e': -0.007082815, 'n': -0.067479069 }},
-56 : { -38 : {'e': 0.001926177, 'n': -0.060995628 },
    -37 : {'e': 0.010007574, 'n': -0.057211472 },
    -36 : {'e': 0.016860266, 'n': -0.054359903 },
    -35 : {'e': 0.023819689, 'n': -0.051544785 },
    -34 : {'e': 0.02294483, 'n': -0.050693387 },
    -33 : {'e': 0.020927739, 'n': -0.051043012 },
    -32 : {'e': 0.017706421, 'n': -0.051622597 },
    -31 : {'e': 0.014732026, 'n': -0.05335408 },
    -30 : {'e': 0.012185592, 'n': -0.054701881 },
    -29 : {'e': 0.010166424, 'n': -0.056323716 },
    -28 : {'e': 0.009283095, 'n': -0.057901184 },
    -27 : {'e': 0.008280855, 'n': -0.059278159 },
    -26 : {'e': 0.005585498, 'n': -0.06045835 },
    -25 : {'e': 0.004175996, 'n': -0.061578982 },
    -24 : {'e': 0.003031365, 'n': -0.062060617 },
    -23 : {'e': 0.003285206, 'n': -0.062937843 },
    -22 : {'e': 0.002872148, 'n': -0.063844283 },
    -21 : {'e': 0.001582585, 'n': -0.065021242 },
    -20 : {'e': -0.000988759, 'n': -0.065814565 }},
-55 : { -37 : {'e': 0.004254428, 'n': -0.057995272 },
    -36 : {'e': 0.012289015, 'n': -0.055016362 },
    -35 : {'e': 0.018710191, 'n': -0.052719246 },
    -34 : {'e': 0.022069322, 'n': -0.051004926 },
    -33 : {'e': 0.020928417, 'n': -0.051238852 },
    -32 : {'e': 0.017782799, 'n': -0.052631683 },
    -31 : {'e': 0.015066947, 'n': -0.054124182 },
    -30 : {'e': 0.013047026, 'n': -0.055696579 },
    -29 : {'e': 0.011348239, 'n': -0.057026038 },
    -28 : {'e': 0.010296999, 'n': -0.057951004 },
    -27 : {'e': 0.008985279, 'n': -0.058849472 },
    -26 : {'e': 0.007412237, 'n': -0.060969759 },
    -25 : {'e': 0.006479561, 'n': -0.061707543 },
    -24 : {'e': 0.006501777, 'n': -0.061545445 },
    -23 : {'e': 0.008020428, 'n': -0.062123453 },
    -22 : {'e': 0.009235945, 'n': -0.063040855 },
    -21 : {'e': 0.007515, 'n': -0.06382596 },
    -20 : {'e': 0.005468454, 'n': -0.065163566 }},
-54 : { -36 : {'e': 0.007308919, 'n': -0.055923979 },
    -35 : {'e': 0.014895109, 'n': -0.053030076 },
    -34 : {'e': 0.021589502, 'n': -0.05036752 },
    -33 : {'e': 0.020546462, 'n': -0.051726971 },
    -32 : {'e': 0.017352094, 'n': -0.053711214 },
    -31 : {'e': 0.015334971, 'n': -0.055706713 },
    -30 : {'e': 0.01279861, 'n': -0.057152939 },
    -29 : {'e': 0.011667695, 'n': -0.058227887 },
    -28 : {'e': 0.010506626, 'n': -0.058146328 },
    -27 : {'e': 0.00896134, 'n': -0.059058702 },
    -26 : {'e': 0.008360895, 'n': -0.060513908 },
    -25 : {'e': 0.007934915, 'n': -0.061239944 },
    -24 : {'e': 0.008625853, 'n': -0.060906772 },
    -23 : {'e': 0.009270293, 'n': -0.060142121 },
    -22 : {'e': 0.0099885, 'n': -0.060615981 },
    -21 : {'e': 0.009979673, 'n': -0.062111476 },
    -20 : {'e': 0.008300329, 'n': -0.063912162 }},
-53 : { -35 : {'e': 0.010382133, 'n': -0.054744865 },
    -34 : {'e': 0.017156396, 'n': -0.053029583 },
    -33 : {'e': 0.01817417, 'n': -0.053687407 },
    -32 : {'e': 0.0163002, 'n': -0.055396785 },
    -31 : {'e': 0.015171504, 'n': -0.057427298 },
    -30 : {'e': 0.013621713, 'n': -0.05909154 },
    -29 : {'e': 0.011929999, 'n': -0.059555614 },
    -28 : {'e': 0.010295458, 'n': -0.059863107 },
    -27 : {'e': 0.00842373, 'n': -0.060485147 },
    -26 : {'e': 0.008457075, 'n': -0.060374835 },
    -25 : {'e': 0.009108462, 'n': -0.060603989 },
    -24 : {'e': 0.009742479, 'n': -0.060629013 },
    -23 : {'e': 0.008790374, 'n': -0.058842921 },
    -22 : {'e': 0.009226117, 'n': -0.058958731 },
    -21 : {'e': 0.010313008, 'n': -0.061330316 },
    -20 : {'e': 0.009455368, 'n': -0.063099933 }},
-52 : { -34 : {'e': 0.009957825, 'n': -0.056279911 },
    -33 : {'e': 0.013127898, 'n': -0.056547341 },
    -32 : {'e': 0.01373188, 'n': -0.057870676 },
    -31 : {'e': 0.015024166, 'n': -0.059497298 },
    -30 : {'e': 0.015222228, 'n': -0.061052992 },
    -29 : {'e': 0.013388381, 'n': -0.06079401 },
    -28 : {'e': 0.011258747, 'n': -0.060444776 },
    -27 : {'e': 0.009607315, 'n': -0.060237641 },
    -26 : {'e': 0.009331768, 'n': -0.059467097 },
    -25 : {'e': 0.010081921, 'n': -0.059725408 },
    -24 : {'e': 0.011497134, 'n': -0.061479686 },
    -23 : {'e': 0.011536576, 'n': -0.061165366 },
    -22 : {'e': 0.011022751, 'n': -0.059997689 },
    -21 : {'e': 0.01091248, 'n': -0.061194945 },
    -20 : {'e': 0.010586864, 'n': -0.062668183 }},
-51 : { -33 : {'e': 0.007807118, 'n': -0.059030728 },
    -32 : {'e': 0.010907528, 'n': -0.059843609 },
    -31 : {'e': 0.013709461, 'n': -0.061576153 },
    -30 : {'e': 0.015591428, 'n': -0.06328013 },
    -29 : {'e': 0.014187906, 'n': -0.061024127 },
    -28 : {'e': 0.012894963, 'n': -0.059631488 },
    -27 : {'e': 0.011611849, 'n': -0.058593473 },
    -26 : {'e': 0.010706385, 'n': -0.058116726 },
    -25 : {'e': 0.010925093, 'n': -0.05841324 },
    -24 : {'e': 0.011677223, 'n': -0.059744681 },
    -23 : {'e': 0.011798346, 'n': -0.060288989 },
    -22 : {'e': 0.012382304, 'n': -0.060250969 },
    -21 : {'e': 0.012016112, 'n': -0.061676912 },
    -20 : {'e': 0.011848747, 'n': -0.062792306 }},
-50 : { -32 : {'e': 0.006723051, 'n': -0.061347169 },
    -31 : {'e': 0.010140604, 'n': -0.061945748 },
    -30 : {'e': 0.012593849, 'n': -0.062487262 },
    -29 : {'e': 0.013042159, 'n': -0.061267931 },
    -28 : {'e': 0.013166537, 'n': -0.059206381 },
    -27 : {'e': 0.012769317, 'n': -0.058122695 },
    -26 : {'e': 0.011902518, 'n': -0.057769617 },
    -25 : {'e': 0.012119289, 'n': -0.057888317 },
    -24 : {'e': 0.011325565, 'n': -0.05845823 },
    -23 : {'e': 0.010318975, 'n': -0.058800866 },
    -22 : {'e': 0.011986423, 'n': -0.060512701 },
    -21 : {'e': 0.013435838, 'n': -0.062342676 },
    -20 : {'e': 0.013538753, 'n': -0.063490324 }},
-49 : { -30 : {'e': 0.009164093, 'n': -0.061967397 },
    -29 : {'e': 0.011508013, 'n': -0.060726638 },
    -28 : {'e': 0.012725602, 'n': -0.059425368 },
    -27 : {'e': 0.012593274, 'n': -0.05839916 },
    -26 : {'e': 0.012841563, 'n': -0.05772341 },
    -25 : {'e': 0.012935076, 'n': -0.057572141 },
    -24 : {'e': 0.01276131, 'n': -0.058038532 },
    -23 : {'e': 0.012528754, 'n': -0.058707781 },
    -22 : {'e': 0.01357572, 'n': -0.060403975 },
    -21 : {'e': 0.01471488, 'n': -0.062445585 },
    -20 : {'e': 0.01478096, 'n': -0.062657906 }},
-48 : { -29 : {'e': 0.008431007, 'n': -0.061068115 },
    -28 : {'e': 0.010497076, 'n': -0.0599899 },
    -27 : {'e': 0.01143754, 'n': -0.058926417 },
    -26 : {'e': 0.012471749, 'n': -0.058124049 },
    -25 : {'e': 0.013213345, 'n': -0.05876048 },
    -24 : {'e': 0.013817227, 'n': -0.057962736 },
    -23 : {'e': 0.014810748, 'n': -0.058501725 },
    -22 : {'e': 0.015402907, 'n': -0.060070333 },
    -21 : {'e': 0.016174297, 'n': -0.061402824 },
    -20 : {'e': 0.0153954, 'n': -0.061705749 }},
-47 : { -28 : {'e': 0.007455292, 'n': -0.06056798 },
    -27 : {'e': 0.009674515, 'n': -0.059333382 },
    -26 : {'e': 0.011372891, 'n': -0.058466027 },
    -25 : {'e': 0.012719786, 'n': -0.05773123 },
    -24 : {'e': 0.014297787, 'n': -0.057098512 },
    -23 : {'e': 0.016296283, 'n': -0.058175049 },
    -22 : {'e': 0.01772492, 'n': -0.059919947 },
    -21 : {'e': 0.01697198, 'n': -0.060602955 },
    -20 : {'e': 0.016166223, 'n': -0.06134573 }},
-46 : { -25 : {'e': 0.012506865, 'n': -0.057909157 },
    -24 : {'e': 0.014466763, 'n': -0.057242184 },
    -23 : {'e': 0.016142884, 'n': -0.058521132 },
    -22 : {'e': 0.018033617, 'n': -0.059684504 },
    -21 : {'e': 0.016885187, 'n': -0.060012765 },
    -20 : {'e': 0.016159866, 'n': -0.061245275 }},
-45 : { -24 : {'e': 0.014100067, 'n': -0.058208636 },
    -23 : {'e': 0.014156961, 'n': -0.058728753 },
    -22 : {'e': 0.01539629, 'n': -0.059380403 },
    -21 : {'e': 0.016766199, 'n': -0.059628828 },
    -20 : {'e': 0.016104204, 'n': -0.060652003 }},
-44 : { -23 : {'e': 0.017569931, 'n': -0.058485371 },
    -22 : {'e': 0.017791431, 'n': -0.058827704 },
    -21 : {'e': 0.0167912, 'n': -0.059394707 },
    -20 : {'e': 0.015935551, 'n': -0.060435665 }},
-43 : { -23 : {'e': 0.020069649, 'n': -0.05862857 },
    -22 : {'e': 0.019781923, 'n': -0.059057516 },
    -21 : {'e': 0.01635317, 'n': -0.059737143 },
    -20 : {'e': 0.016000567, 'n': -0.061165166 }},
-42 : { -23 : {'e': 0.018545608, 'n': -0.06091561 },
    -22 : {'e': 0.020649511, 'n': -0.061080471 },
    -21 : {'e': 0.019235976, 'n': -0.061637231 },
    -20 : {'e': 0.017115687, 'n': -0.062750496 }},
-41 : { -23 : {'e': 0.015962045, 'n': -0.063017783 },
    -22 : {'e': 0.020094381, 'n': -0.063333095 },
    -21 : {'e': 0.02007934, 'n': -0.063631575 },
    -20 : {'e': 0.018380154, 'n': -0.064336182 }}
}
