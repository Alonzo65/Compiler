ZERO .INT #0
ONE .INT #1
NULLTERM .BYT '\0'
lablit0 .BYT ','
lablit1 .BYT ' '
lablit2 .INT #0
lablit3 .INT #1
lablit4 .INT #2
lablit15 .BYT 'l'
lablit18 .INT #10
lablit19 .INT #34
lablit20 .INT #20
lablit21 .INT #4181
lablit22 .INT #25
lablit23 .INT #46368
lablit24 .INT #47
lablit25 .INT #1836311903
lablit29 .BYT '\n'
lablit30 .BYT 'f'
lablit32 .BYT 'a'
lablit33 .BYT 'i'
lablit34 .BYT ':'
lablit35 .BYT '('
lablit36 .INT #367
lablit37 .BYT 'p'
lablit38 .INT #8
lablit43 .BYT 's'
lablit44 .BYT 'u'
lablit45 .BYT 'c'
lablit46 .BYT 'e'
lablit49 .BYT '!'
lablit55 .BYT 
lablit60 .BYT 'C'
lablit61 .BYT 'q'
lablit62 .INT #4
lablit64 .INT #3
lablit65 .INT #83
lablit67 .BYT 'r'
lablit69 .BYT '-'
lablit80 .BYT '&'
lablit84 .INT #23
lablit86 .INT #12
lablit90 .BYT 'I'
 .BYT 'n'
 .BYT 'p'
 .BYT 'u'
 .BYT 't'
 .BYT ' '
 .BYT 'n'
 .BYT 'u'
 .BYT 'm'
 .BYT 'b'
 .BYT 'e'
 .BYT 'r'
 .BYT ' '
 .BYT 'o'
 .BYT 'f'
 .BYT ' '
 .BYT 'i'
 .BYT 't'
 .BYT 'e'
 .BYT 'r'
 .BYT 'a'
 .BYT 't'
 .BYT 'i'
 .BYT 'o'
 .BYT 'n'
 .BYT 's'
 .BYT ':'
 .BYT '\0'
lablit96 .BYT 'n'
lablit98 .BYT 't'
lablit99 .BYT 'h'
lablit114 .BYT 'z'
lablit117 .BYT 'd'
lablit125 .BYT 'm'
lablit127 .BYT 'o'
lablit136 .BYT 'x'
lablit140 .BYT 'y'
lablit141 .BYT '\t'
lablit143 .INT #38
lablit144 .INT #37
lablit145 .INT #40
lablit146 .INT #9
lablit147 .INT #44
lablit148 .INT #5
lablit150 .INT #15466
lablit162 .BYT 'E'
 .BYT 'Z'
 .BYT ' '
 .BYT 'D'
 .BYT 'u'
 .BYT 'b'
 .BYT 's'
 .BYT ' '
 .BYT 'M'
 .BYT 'i'
 .BYT 'g'
 .BYT 'u'
 .BYT 'e'
 .BYT 'l'
 .BYT '\0'
 JMP MAIN
MAIN MOV R4, FP
 MOV FP, SP
 ADI SP, #-4
 STR R4, SP
 ADI SP, #-324
 MOV R5, PC
 ADI R5, #36
 STR R5, FP
 JMP global_main
 TRP #0
global_main ADI R3, #0
 MOV R2, FP
 ADI R2, #-8
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-12
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-16
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-20
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-21
 LDR R1, ZERO
 STB R1, R2
 MOV R2, FP
 ADI R2, #-22
 LDR R1, ZERO
 STB R1, R2
 MOV R2, FP
 ADI R2, #-26
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-27
 LDR R1, ZERO
 STB R1, R2
 MOV R2, FP
 ADI R2, #-28
 LDR R1, ZERO
 STB R1, R2
 MOV R2, FP
 ADI R2, #-29
 LDR R1, ZERO
 STB R1, R2
 MOV R2, FP
 ADI R2, #-30
 LDR R1, ZERO
 STB R1, R2
 MOV R2, FP
 ADI R2, #-31
 LDR R1, ZERO
 STB R1, R2
 MOV R2, FP
 ADI R2, #-35
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-36
 LDR R1, ZERO
 STB R1, R2
 MOV R2, FP
 ADI R2, #-40
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-41
 LDR R1, ZERO
 STB R1, R2
 MOV R2, FP
 ADI R2, #-42
 LDR R1, ZERO
 STB R1, R2
 MOV R2, FP
 ADI R2, #-43
 LDR R1, ZERO
 STB R1, R2
 MOV R2, FP
 ADI R2, #-44
 LDR R1, ZERO
 STB R1, R2
 MOV R2, FP
 ADI R2, #-45
 LDR R1, ZERO
 STB R1, R2
 MOV R2, FP
 ADI R2, #-49
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-50
 LDR R1, ZERO
 STB R1, R2
 MOV R2, FP
 ADI R2, #-51
 LDR R1, ZERO
 STB R1, R2
 MOV R2, FP
 ADI R2, #-55
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-59
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-63
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-67
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-71
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-75
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-79
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-83
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-87
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-91
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-95
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-99
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-103
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-107
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-111
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-115
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-119
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-123
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-127
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-131
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-135
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-139
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-143
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-147
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-151
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-155
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-159
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-163
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-167
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-171
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-175
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-179
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-183
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-187
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-191
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-195
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-199
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-200
 LDR R1, ZERO
 STB R1, R2
 MOV R2, FP
 ADI R2, #-204
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-208
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-212
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-216
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-220
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-224
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-228
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-232
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-236
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-240
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-244
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-248
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-252
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-256
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-260
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-264
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-268
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-272
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-276
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-280
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-284
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-288
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-292
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-296
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-300
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-304
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-308
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-312
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-316
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-320
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-324
 LDR R1, ZERO
 STR R1, R2
 LDR R1, ZERO
 LDR R1, lablit2
 MOV R0, FP
 ADI R0, #-12
 STR R1, R0
 LDR R1, lablit3
 LDR R0, ZERO
 ADI R0, #-1
 MUL R1, R0
exit_label67 ADI R3, #0
 MOV R0, FP
 ADI R0, #-91
 STR R1, R0
 MOV R1, FP
 ADI R1, #-91
 LDR R1, R1
 MOV R0, FP
 ADI R0, #-16
 STR R1, R0
 LDR R1, lablit4
 LDR R0, ZERO
 ADI R0, #-1
 MUL R1, R0
exit_label68 ADI R3, #0
 MOV R0, FP
 ADI R0, #-95
 STR R1, R0
 MOV R1, FP
 ADI R1, #-95
 LDR R1, R1
 MOV R0, FP
 ADI R0, #-20
 STR R1, R0
 LDB R1, lablit60
 MOV R0, FP
 ADI R0, #-21
 STB R1, R0
 LDB R1, lablit61
 MOV R0, FP
 ADI R0, #-22
 STB R1, R0
 LDR R0, lablit62
 LDR R1, lablit4
 MUL R1, R0
 MOV R0, FP
 ADI R0, #-99
 STR R1, R0
 LDR R0, lablit64
 MOV R1, FP
 ADI R1, #-99
 LDR R1, R1
 ADD R1, R0
 MOV R0, FP
 ADI R0, #-103
 STR R1, R0
 LDR R0, lablit65
 LDR R1, lablit64
 DIV R0, R1
 MOV R1, R0
 MOV R0, FP
 ADI R0, #-107
 STR R1, R0
 MOV R0, FP
 ADI R0, #-103
 LDR R0, R0
 MOV R1, FP
 ADI R1, #-107
 LDR R1, R1
 ADD R1, R0
 MOV R0, FP
 ADI R0, #-111
 STR R1, R0
 MOV R1, FP
 ADI R1, #-111
 LDR R1, R1
 MOV R0, FP
 ADI R0, #-26
 STR R1, R0
 LDB R1, lablit67
 MOV R0, FP
 ADI R0, #-27
 STB R1, R0
 LDB R1, lablit1
 MOV R0, FP
 ADI R0, #-28
 STB R1, R0
 LDB R1, lablit69
 MOV R0, FP
 ADI R0, #-29
 STB R1, R0
 LDB R1, lablit29
 MOV R0, FP
 ADI R0, #-30
 STB R1, R0
 LDB R1, lablit43
 MOV R0, FP
 ADI R0, #-31
 STB R1, R0
 LDR R1, lablit2
 MOV R0, FP
 ADI R0, #-35
 STR R1, R0
 LDB R1, lablit44
 MOV R0, FP
 ADI R0, #-36
 STB R1, R0
 LDR R1, lablit2
 MOV R0, FP
 ADI R0, #-40
 STR R1, R0
 LDB R1, lablit45
 MOV R0, FP
 ADI R0, #-41
 STB R1, R0
 LDB R1, lablit46
 MOV R0, FP
 ADI R0, #-42
 STB R1, R0
 LDR R1, ZERO
 LDB R1, lablit30
 MOV R0, FP
 ADI R0, #-44
 STB R1, R0
 LDB R1, lablit15
 MOV R0, FP
 ADI R0, #-45
 STB R1, R0
 LDR R1, ZERO
 LDB R1, lablit0
 MOV R0, FP
 ADI R0, #-50
 STB R1, R0
 LDB R1, lablit80
 MOV R0, FP
 ADI R0, #-51
 STB R1, R0
 LDR R1, lablit2
 MOV R0, FP
 ADI R0, #-55
 STR R1, R0
 MOV R0, FP
 ADI R0, #-26
 LDR R0, R0
 LDR R1, lablit4
 ADD R1, R0
 MOV R0, FP
 ADI R0, #-115
 STR R1, R0
 LDR R1, lablit4
 LDR R0, ZERO
 ADI R0, #-1
 MUL R1, R0
exit_label69 ADI R3, #0
 MOV R0, FP
 ADI R0, #-119
 STR R1, R0
 MOV R0, FP
 ADI R0, #-26
 LDR R0, R0
 MOV R1, FP
 ADI R1, #-119
 LDR R1, R1
 MUL R1, R0
 MOV R0, FP
 ADI R0, #-123
 STR R1, R0
 MOV R0, FP
 ADI R0, #-115
 LDR R0, R0
 MOV R1, FP
 ADI R1, #-123
 LDR R1, R1
 DIV R0, R1
 MOV R1, R0
 MOV R0, FP
 ADI R0, #-127
 STR R1, R0
 LDR R1, lablit84
 LDR R0, ZERO
 ADI R0, #-1
 MUL R1, R0
exit_label70 ADI R3, #0
 MOV R0, FP
 ADI R0, #-131
 STR R1, R0
 MOV R0, FP
 ADI R0, #-127
 LDR R0, R0
 MOV R1, FP
 ADI R1, #-131
 LDR R1, R1
 ADD R1, R0
 MOV R0, FP
 ADI R0, #-135
 STR R1, R0
 LDR R1, lablit4
 LDR R2, ZERO
 CMP R2, R1
 BLT R2, exit_label71
 BRZ R2, exit_label71
 LDR R2, ZERO
 ADI R2, #-1
 MUL R1, R2
exit_label71 ADI R3, #0
 MOV R0, FP
 ADI R0, #-139
 STR R1, R0
 MOV R0, FP
 ADI R0, #-135
 LDR R0, R0
 MOV R1, FP
 ADI R1, #-139
 LDR R1, R1
 SUB R0, R1
 MOV R1, R0
 MOV R0, FP
 ADI R0, #-143
 STR R1, R0
 LDR R1, lablit86
 LDR R0, ZERO
 ADI R0, #-1
 MUL R1, R0
exit_label72 ADI R3, #0
 MOV R0, FP
 ADI R0, #-147
 STR R1, R0
 MOV R0, FP
 ADI R0, #-143
 LDR R0, R0
 MOV R1, FP
 ADI R1, #-147
 LDR R1, R1
 ADD R1, R0
 MOV R0, FP
 ADI R0, #-151
 STR R1, R0
 MOV R1, FP
 ADI R1, #-151
 LDR R1, R1
 MOV R0, FP
 ADI R0, #-59
 STR R1, R0
 LDR R1, lablit2
 MOV R0, FP
 ADI R0, #-63
 STR R1, R0
 LDR R1, lablit2
 MOV R0, FP
 ADI R0, #-67
 STR R1, R0
 LDR R1, lablit3
 MOV R0, FP
 ADI R0, #-71
 STR R1, R0
 LDA R1, lablit90
output_string0 LDB R3, R1
 LDB R2, NULLTERM
 CMP R2, R3
 BRZ R2, exit_string0
 TRP #3
 ADI R1, #1
 JMP output_string0
exit_string0 ADI R3, #0
 MOV R1, FP
 ADI R1, #-30
 LDB R1, R1
 MOV R3, R1
 TRP #3
 TRP #2
 MOV R1, FP
 ADI R1, #-49
 STR R3, R1
 MOV R1, FP
 ADI R1, #-49
 LDR R1, R1
 MOV R3, R1
 TRP #1
 MOV R1, FP
 ADI R1, #-30
 LDB R1, R1
 MOV R3, R1
 TRP #3
while_loop1 ADI R3, #0
 MOV R0, FP
 ADI R0, #-49
 LDR R0, R0
 LDR R1, lablit2
 CMP R0, R1
 BGT R0, trueexit_label74
 BRZ R0, trueexit_label74
 LDR R1, ZERO
 JMP false_label73
trueexit_label74 LDR R1, ONE
false_label73 ADI R3, #0
 MOV R0, FP
 ADI R0, #-155
 STR R1, R0
 MOV R1, FP
 ADI R1, #-155
 LDR R1, R1
 BRZ R1, if_label19
 LDR R1, lablit2
 MOV R0, FP
 ADI R0, #-55
 STR R1, R0
 MOV R1, FP
 ADI R1, #-8
 LDR R1, R1
 MOV R2, SP
 ADI R2, #-8
 STR R1, R2
 MOV R1, FP
 ADI R1, #-49
 LDR R1, R1
 MOV R2, SP
 ADI R2, #-12
 STR R1, R2
 LDR R1, lablit2
 MOV R2, SP
 ADI R2, #-16
 STR R1, R2
 MOV R1, FP
 ADI R1, #-16
 LDR R1, R1
 MOV R2, SP
 ADI R2, #-20
 STR R1, R2
 MOV R1, FP
 ADI R1, #-20
 LDR R1, R1
 MOV R2, SP
 ADI R2, #-24
 STR R1, R2
 MOV R1, FP
 ADI R1, #-12
 LDR R1, R1
 MOV R2, SP
 ADI R2, #-28
 STR R1, R2
 MOV R1, FP
 ADI R1, #-55
 LDR R1, R1
 MOV R2, SP
 ADI R2, #-32
 STR R1, R2
 MOV R1, FP
 ADI R1, #-45
 LDB R1, R1
 MOV R2, SP
 ADI R2, #-33
 STR R1, R2
 MOV R4, FP
 MOV FP, SP
 ADI SP, #-4
 STR R4, SP
 ADI SP, #-183
 MOV R5, PC
 ADI R5, #36
 STR R5, FP
 JMP Functions_fibonacciSequence
 LDR R1, SP
 MOV R0, FP
 ADI R0, #-159
 STR R1, R0
 MOV R1, FP
 ADI R1, #-159
 LDR R1, R1
 MOV R0, FP
 ADI R0, #-55
 STR R1, R0
 MOV R1, FP
 ADI R1, #-30
 LDB R1, R1
 MOV R3, R1
 TRP #3
 TRP #2
 MOV R1, FP
 ADI R1, #-49
 STR R3, R1
 MOV R1, FP
 ADI R1, #-49
 LDR R1, R1
 MOV R3, R1
 TRP #1
 MOV R1, FP
 ADI R1, #-30
 LDB R1, R1
 MOV R3, R1
 TRP #3
 JMP while_loop1
if_label19 ADI R3, #0
while_exit0 ADI R3, #0
 MOV R1, FP
 ADI R1, #-30
 LDB R1, R1
 MOV R3, R1
 TRP #3
 LDB R1, lablit29
 MOV R3, R1
 TRP #3
 MOV R1, FP
 ADI R1, #-51
 LDB R1, R1
 MOV R3, R1
 TRP #3
 MOV R1, FP
 ADI R1, #-30
 LDB R1, R1
 MOV R3, R1
 TRP #3
 LDB R1, lablit33
 MOV R3, R1
 TRP #3
 LDB R1, lablit96
 MOV R3, R1
 TRP #3
 LDB R1, lablit37
 MOV R3, R1
 TRP #3
 MOV R1, FP
 ADI R1, #-36
 LDB R1, R1
 MOV R3, R1
 TRP #3
 LDB R1, lablit98
 MOV R3, R1
 TRP #3
 MOV R1, FP
 ADI R1, #-28
 LDB R1, R1
 MOV R3, R1
 TRP #3
 MOV R1, FP
 ADI R1, #-41
 LDB R1, R1
 MOV R3, R1
 TRP #3
 LDB R1, lablit99
 MOV R0, FP
 ADI R0, #-41
 STB R1, R0
 MOV R1, FP
 ADI R1, #-41
 LDB R1, R1
 MOV R3, R1
 TRP #3
 LDB R1, lablit45
 MOV R0, FP
 ADI R0, #-41
 STB R1, R0
 LDB R1, lablit32
 MOV R3, R1
 TRP #3
 MOV R1, FP
 ADI R1, #-27
 LDB R1, R1
 MOV R3, R1
 TRP #3
 LDB R1, lablit34
 MOV R3, R1
 TRP #3
 MOV R1, FP
 ADI R1, #-30
 LDB R1, R1
 MOV R3, R1
 TRP #3
 TRP #4
 MOV R1, FP
 ADI R1, #-51
 STB R3, R1
 TRP #4
 MOV R1, FP
 ADI R1, #-43
 STB R3, R1
 MOV R1, FP
 ADI R1, #-51
 LDB R1, R1
 MOV R3, R1
 TRP #3
 MOV R1, FP
 ADI R1, #-43
 LDB R1, R1
 MOV R3, R1
 TRP #3
 MOV R1, FP
 ADI R1, #-30
 LDB R1, R1
 MOV R3, R1
 TRP #3
 MOV R0, FP
 ADI R0, #-51
 LDB R0, lablit32
 MOV R1, FP
 ADI R1, #-51
 LDB R1, R1
 CMP R0, R1
 BNZ R0, false_label75
 LDR R1, ONE
 JMP trueexit_label76
false_label75 LDR R1, ZERO
trueexit_label76 ADI R3, #0
 MOV R0, FP
 ADI R0, #-163
 STB R1, R0
 MOV R1, FP
 ADI R1, #-163
 LDR R1, R1
 MOV R0, FP
 ADI R0, #-75
 STR R1, R0
 MOV R1, FP
 ADI R1, #-75
 LDR R1, R1
 BRZ R1, if_label22
 LDB R1, lablit43
 MOV R3, R1
 TRP #3
 LDB R1, lablit98
 MOV R3, R1
 TRP #3
 LDB R1, lablit32
 MOV R3, R1
 TRP #3
 LDB R1, lablit67
 MOV R3, R1
 TRP #3
 LDB R1, lablit98
 MOV R3, R1
 TRP #3
 MOV R1, FP
 ADI R1, #-30
 LDB R1, R1
 MOV R3, R1
 TRP #3
 MOV R0, FP
 ADI R0, #-63
 LDR R0, R0
 LDR R1, lablit3
 CMP R0, R1
 BNZ R0, false_label77
 LDR R1, ONE
 JMP trueexit_label78
false_label77 LDR R1, ZERO
trueexit_label78 ADI R3, #0
 MOV R0, FP
 ADI R0, #-167
 STR R1, R0
 MOV R1, FP
 ADI R1, #-167
 LDR R1, R1
 BRZ R1, if_label20
 LDR R1, lablit2
 MOV R0, FP
 ADI R0, #-63
 STR R1, R0
 JMP if_exitlabel21
if_label20 ADI R3, #0
 LDR R1, lablit3
 MOV R0, FP
 ADI R0, #-63
 STR R1, R0
if_exitlabel21 ADI R3, #0
 LDR R1, lablit2
 MOV R0, FP
 ADI R0, #-71
 STR R1, R0
 MOV R0, FP
 ADI R0, #-67
 LDR R0, R0
 LDR R1, lablit3
 ADD R1, R0
 MOV R0, FP
 ADI R0, #-171
 STR R1, R0
 MOV R1, FP
 ADI R1, #-171
 LDR R1, R1
 MOV R0, FP
 ADI R0, #-67
 STR R1, R0
 JMP switch_exit0
if_label22 ADI R3, #0
 LDB R0, lablit114
 MOV R1, FP
 ADI R1, #-51
 LDB R1, R1
 CMP R0, R1
 BNZ R0, false_label79
 LDR R1, ONE
 JMP trueexit_label80
false_label79 LDR R1, ZERO
trueexit_label80 ADI R3, #0
 MOV R0, FP
 ADI R0, #-175
 STB R1, R0
 MOV R1, FP
 ADI R1, #-175
 LDR R1, R1
 MOV R0, FP
 ADI R0, #-79
 STR R1, R0
 MOV R1, FP
 ADI R1, #-79
 LDR R1, R1
 BRZ R1, if_label25
 LDB R1, lablit46
 MOV R3, R1
 TRP #3
 LDB R1, lablit96
 MOV R3, R1
 TRP #3
 LDB R1, lablit117
 MOV R3, R1
 TRP #3
 MOV R1, FP
 ADI R1, #-30
 LDB R1, R1
 MOV R3, R1
 TRP #3
 MOV R0, FP
 ADI R0, #-63
 LDR R0, R0
 LDR R1, lablit3
 CMP R0, R1
 BNZ R0, false_label81
 LDR R1, ONE
 JMP trueexit_label82
false_label81 LDR R1, ZERO
trueexit_label82 ADI R3, #0
 MOV R0, FP
 ADI R0, #-179
 STR R1, R0
 MOV R1, FP
 ADI R1, #-179
 LDR R1, R1
 BRZ R1, if_label23
 LDR R1, lablit2
 MOV R0, FP
 ADI R0, #-63
 STR R1, R0
 JMP if_exitlabel24
if_label23 ADI R3, #0
 LDR R1, lablit3
 MOV R0, FP
 ADI R0, #-63
 STR R1, R0
if_exitlabel24 ADI R3, #0
 LDR R1, lablit2
 MOV R0, FP
 ADI R0, #-71
 STR R1, R0
 MOV R0, FP
 ADI R0, #-67
 LDR R0, R0
 LDR R1, lablit3
 ADD R1, R0
 MOV R0, FP
 ADI R0, #-183
 STR R1, R0
 MOV R1, FP
 ADI R1, #-183
 LDR R1, R1
 MOV R0, FP
 ADI R0, #-67
 STR R1, R0
 JMP switch_exit0
if_label25 ADI R3, #0
 LDB R0, lablit15
 MOV R1, FP
 ADI R1, #-51
 LDB R1, R1
 CMP R0, R1
 BNZ R0, false_label83
 LDR R1, ONE
 JMP trueexit_label84
false_label83 LDR R1, ZERO
trueexit_label84 ADI R3, #0
 MOV R0, FP
 ADI R0, #-187
 STB R1, R0
 MOV R1, FP
 ADI R1, #-187
 LDR R1, R1
 MOV R0, FP
 ADI R0, #-83
 STR R1, R0
 MOV R1, FP
 ADI R1, #-83
 LDR R1, R1
 BRZ R1, if_label28
 LDB R1, lablit46
 MOV R3, R1
 TRP #3
 MOV R1, FP
 ADI R1, #-45
 LDB R1, R1
 MOV R3, R1
 TRP #3
 MOV R1, FP
 ADI R1, #-42
 LDB R1, R1
 MOV R3, R1
 TRP #3
 LDB R1, lablit125
 MOV R3, R1
 TRP #3
 LDB R1, lablit33
 MOV R3, R1
 TRP #3
 LDB R1, lablit127
 MOV R3, R1
 TRP #3
 LDB R1, lablit37
 MOV R3, R1
 TRP #3
 LDB R1, lablit46
 MOV R3, R1
 TRP #3
 LDB R1, lablit46
 MOV R3, R1
 TRP #3
 MOV R1, FP
 ADI R1, #-30
 LDB R1, R1
 MOV R3, R1
 TRP #3
 MOV R0, FP
 ADI R0, #-63
 LDR R0, R0
 LDR R1, lablit3
 CMP R0, R1
 BNZ R0, false_label85
 LDR R1, ONE
 JMP trueexit_label86
false_label85 LDR R1, ZERO
trueexit_label86 ADI R3, #0
 MOV R0, FP
 ADI R0, #-191
 STR R1, R0
 MOV R1, FP
 ADI R1, #-191
 LDR R1, R1
 BRZ R1, if_label26
 LDR R1, lablit2
 MOV R0, FP
 ADI R0, #-63
 STR R1, R0
 JMP if_exitlabel27
if_label26 ADI R3, #0
 LDR R1, lablit3
 MOV R0, FP
 ADI R0, #-63
 STR R1, R0
if_exitlabel27 ADI R3, #0
 LDR R1, lablit2
 MOV R0, FP
 ADI R0, #-71
 STR R1, R0
 MOV R0, FP
 ADI R0, #-67
 LDR R0, R0
 LDR R1, lablit3
 ADD R1, R0
 MOV R0, FP
 ADI R0, #-195
 STR R1, R0
 MOV R1, FP
 ADI R1, #-195
 LDR R1, R1
 MOV R0, FP
 ADI R0, #-67
 STR R1, R0
 JMP switch_exit0
if_label28 ADI R3, #0
 MOV R0, FP
 ADI R0, #-51
 LDB R0, lablit136
 MOV R1, FP
 ADI R1, #-51
 LDB R1, R1
 CMP R0, R1
 BNZ R0, false_label87
 LDR R1, ONE
 JMP trueexit_label88
false_label87 LDR R1, ZERO
trueexit_label88 ADI R3, #0
 MOV R0, FP
 ADI R0, #-199
 STB R1, R0
 MOV R1, FP
 ADI R1, #-199
 LDR R1, R1
 MOV R0, FP
 ADI R0, #-87
 STR R1, R0
 MOV R1, FP
 ADI R1, #-87
 LDR R1, R1
 BRZ R1, if_label29
 LDB R1, lablit136
 MOV R3, R1
 TRP #3
 MOV R1, FP
 ADI R1, #-29
 LDB R1, R1
 MOV R3, R1
 TRP #3
 LDB R1, lablit67
 MOV R3, R1
 TRP #3
 LDB R1, lablit32
 MOV R3, R1
 TRP #3
 LDB R1, lablit140
 MOV R3, R1
 TRP #3
 MOV R1, FP
 ADI R1, #-30
 LDB R1, R1
 MOV R3, R1
 TRP #3
 JMP switch_exit1
if_label29 ADI R3, #0
 JMP switch_exit1
switch_exit1 ADI R3, #0
switch_exit0 ADI R3, #0
 MOV R1, FP
 ADI R1, #-43
 LDB R1, R1
 MOV R3, R1
 TRP #3
 MOV R1, FP
 ADI R1, #-43
 LDB R1, R1
 MOV R3, R1
 TRP #3
 MOV R1, FP
 ADI R1, #-22
 LDB R1, R1
 MOV R3, R1
 TRP #3
 MOV R1, FP
 ADI R1, #-27
 LDB R1, R1
 MOV R3, R1
 TRP #3
 MOV R1, FP
 ADI R1, #-21
 LDB R1, R1
 MOV R0, FP
 ADI R0, #-27
 STB R1, R0
 MOV R0, FP
 ADI R0, #-22
 STB R1, R0
 MOV R0, FP
 ADI R0, #-200
 STB R1, R0
 MOV R0, FP
 ADI R0, #-200
 LDB R1, lablit141
 MOV R3, R1
 TRP #3
 MOV R1, FP
 ADI R1, #-22
 LDB R1, R1
 MOV R3, R1
 TRP #3
 MOV R1, FP
 ADI R1, #-27
 LDB R1, R1
 MOV R3, R1
 TRP #3
 LDB R1, lablit29
 MOV R3, R1
 TRP #3
 MOV R1, FP
 ADI R1, #-26
 LDR R1, R1
 MOV R3, R1
 TRP #1
 MOV R1, FP
 ADI R1, #-30
 LDB R1, R1
 MOV R3, R1
 TRP #3
 MOV R1, FP
 ADI R1, #-59
 LDR R1, R1
 MOV R3, R1
 TRP #1
 MOV R1, FP
 ADI R1, #-43
 LDB R1, R1
 MOV R3, R1
 TRP #3
 MOV R0, FP
 ADI R0, #-26
 LDR R0, R0
 LDR R1, lablit143
 CMP R0, R1
 BNZ R0, false_label89
 LDR R1, ONE
 JMP trueexit_label90
false_label89 LDR R1, ZERO
trueexit_label90 ADI R3, #0
 MOV R0, FP
 ADI R0, #-204
 STR R1, R0
 MOV R1, FP
 ADI R1, #-204
 LDR R1, R1
 BRZ R1, if_label32
 LDR R1, lablit144
 LDR R0, ZERO
 ADI R0, #-1
 MUL R1, R0
exit_label91 ADI R3, #0
 MOV R0, FP
 ADI R0, #-208
 STR R1, R0
 MOV R0, FP
 ADI R0, #-59
 LDR R0, R0
 MOV R1, FP
 ADI R1, #-208
 LDR R1, R1
 CMP R0, R1
 BNZ R0, false_label92
 LDR R1, ONE
 JMP trueexit_label93
false_label92 LDR R1, ZERO
trueexit_label93 ADI R3, #0
 MOV R0, FP
 ADI R0, #-212
 STR R1, R0
 MOV R1, FP
 ADI R1, #-212
 LDR R1, R1
 BRZ R1, if_label30
 LDR R0, lablit145
 LDR R1, lablit146
 SUB R0, R1
 MOV R1, R0
 MOV R0, FP
 ADI R0, #-216
 STR R1, R0
 LDR R0, lablit147
 MOV R1, FP
 ADI R1, #-216
 LDR R1, R1
 DIV R0, R1
 MOV R1, R0
 MOV R0, FP
 ADI R0, #-220
 STR R1, R0
 LDR R1, lablit148
 LDR R2, ZERO
 CMP R2, R1
 BLT R2, exit_label94
 BRZ R2, exit_label94
 LDR R2, ZERO
 ADI R2, #-1
 MUL R1, R2
exit_label94 ADI R3, #0
 MOV R0, FP
 ADI R0, #-224
 STR R1, R0
 LDR R1, lablit148
 LDR R0, ZERO
 ADI R0, #-1
 MUL R1, R0
exit_label95 ADI R3, #0
 MOV R0, FP
 ADI R0, #-228
 STR R1, R0
 MOV R0, FP
 ADI R0, #-224
 LDR R0, R0
 MOV R1, FP
 ADI R1, #-228
 LDR R1, R1
 SUB R0, R1
 MOV R1, R0
 MOV R0, FP
 ADI R0, #-232
 STR R1, R0
 MOV R0, FP
 ADI R0, #-220
 LDR R0, R0
 MOV R1, FP
 ADI R1, #-232
 LDR R1, R1
 ADD R1, R0
 MOV R0, FP
 ADI R0, #-236
 STR R1, R0
 MOV R0, FP
 ADI R0, #-59
 LDR R0, R0
 MOV R1, FP
 ADI R1, #-236
 LDR R1, R1
 MUL R1, R0
 MOV R0, FP
 ADI R0, #-240
 STR R1, R0
 MOV R0, FP
 ADI R0, #-26
 LDR R0, R0
 MOV R1, FP
 ADI R1, #-240
 LDR R1, R1
 MUL R1, R0
 MOV R0, FP
 ADI R0, #-244
 STR R1, R0
 MOV R1, FP
 ADI R1, #-244
 LDR R1, R1
 MOV R0, FP
 ADI R0, #-59
 STR R1, R0
if_label30 ADI R3, #0
 LDR R1, lablit150
 LDR R0, ZERO
 ADI R0, #-1
 MUL R1, R0
exit_label96 ADI R3, #0
 MOV R0, FP
 ADI R0, #-248
 STR R1, R0
 MOV R0, FP
 ADI R0, #-59
 LDR R0, R0
 MOV R1, FP
 ADI R1, #-248
 LDR R1, R1
 CMP R0, R1
 BNZ R0, false_label97
 LDR R1, ONE
 JMP trueexit_label98
false_label97 LDR R1, ZERO
trueexit_label98 ADI R3, #0
 MOV R0, FP
 ADI R0, #-252
 STR R1, R0
 MOV R1, FP
 ADI R1, #-252
 LDR R1, R1
 BRZ R1, if_label31
 LDR R1, lablit3
 MOV R0, FP
 ADI R0, #-35
 STR R1, R0
if_label31 ADI R3, #0
 MOV R1, FP
 ADI R1, #-59
 LDR R1, R1
 MOV R3, R1
 TRP #1
 MOV R1, FP
 ADI R1, #-30
 LDB R1, R1
 MOV R3, R1
 TRP #3
if_label32 ADI R3, #0
 MOV R0, FP
 ADI R0, #-55
 LDR R0, R0
 LDR R1, lablit3
 CMP R0, R1
 BNZ R0, false_label99
 LDR R1, ONE
 JMP trueexit_label100
false_label99 LDR R1, ZERO
trueexit_label100 ADI R3, #0
 MOV R0, FP
 ADI R0, #-256
 STR R1, R0
 MOV R0, FP
 ADI R0, #-35
 LDR R0, R0
 LDR R1, lablit3
 CMP R0, R1
 BNZ R0, false_label101
 LDR R1, ONE
 JMP trueexit_label102
false_label101 LDR R1, ZERO
trueexit_label102 ADI R3, #0
 MOV R0, FP
 ADI R0, #-260
 STR R1, R0
 MOV R0, FP
 ADI R0, #-256
 LDR R0, R0
 MOV R1, FP
 ADI R1, #-260
 LDR R1, R1
 LDR R2, ONE
 CMP R2, R1
 BGT R2, false_label103
 CMP R0, R1
 BLT R0, false_label103
 LDR R1, ONE
 JMP trueexit_label104
false_label103 LDR R1, ZERO
trueexit_label104 ADI R3, #0
 MOV R0, FP
 ADI R0, #-264
 STR R1, R0
 MOV R0, FP
 ADI R0, #-63
 LDR R0, R0
 LDR R1, lablit3
 CMP R0, R1
 BNZ R0, false_label105
 LDR R1, ONE
 JMP trueexit_label106
false_label105 LDR R1, ZERO
trueexit_label106 ADI R3, #0
 MOV R0, FP
 ADI R0, #-268
 STR R1, R0
 MOV R0, FP
 ADI R0, #-71
 LDR R0, R0
 LDR R1, lablit2
 CMP R0, R1
 BNZ R0, false_label107
 LDR R1, ONE
 JMP trueexit_label108
false_label107 LDR R1, ZERO
trueexit_label108 ADI R3, #0
 MOV R0, FP
 ADI R0, #-272
 STR R1, R0
 MOV R0, FP
 ADI R0, #-268
 LDR R0, R0
 MOV R1, FP
 ADI R1, #-272
 LDR R1, R1
 LDR R2, ONE
 CMP R2, R1
 BGT R2, false_label109
 CMP R0, R1
 BLT R0, false_label109
 LDR R1, ONE
 JMP trueexit_label110
false_label109 LDR R1, ZERO
trueexit_label110 ADI R3, #0
 MOV R0, FP
 ADI R0, #-276
 STR R1, R0
 MOV R0, FP
 ADI R0, #-67
 LDR R0, R0
 LDR R1, lablit3
 CMP R0, R1
 BNZ R0, false_label111
 LDR R1, ONE
 JMP trueexit_label112
false_label111 LDR R1, ZERO
trueexit_label112 ADI R3, #0
 MOV R0, FP
 ADI R0, #-280
 STR R1, R0
 MOV R0, FP
 ADI R0, #-276
 LDR R0, R0
 MOV R1, FP
 ADI R1, #-280
 LDR R1, R1
 LDR R2, ONE
 CMP R2, R1
 BGT R2, false_label113
 CMP R0, R1
 BLT R0, false_label113
 LDR R1, ONE
 JMP trueexit_label114
false_label113 LDR R1, ZERO
trueexit_label114 ADI R3, #0
 MOV R0, FP
 ADI R0, #-284
 STR R1, R0
 MOV R0, FP
 ADI R0, #-63
 LDR R0, R0
 LDR R1, lablit2
 CMP R0, R1
 BNZ R0, false_label115
 LDR R1, ONE
 JMP trueexit_label116
false_label115 LDR R1, ZERO
trueexit_label116 ADI R3, #0
 MOV R0, FP
 ADI R0, #-288
 STR R1, R0
 MOV R0, FP
 ADI R0, #-71
 LDR R0, R0
 LDR R1, lablit3
 CMP R0, R1
 BNZ R0, false_label117
 LDR R1, ONE
 JMP trueexit_label118
false_label117 LDR R1, ZERO
trueexit_label118 ADI R3, #0
 MOV R0, FP
 ADI R0, #-292
 STR R1, R0
 MOV R0, FP
 ADI R0, #-288
 LDR R0, R0
 MOV R1, FP
 ADI R1, #-292
 LDR R1, R1
 LDR R2, ONE
 CMP R2, R1
 BGT R2, false_label119
 CMP R0, R1
 BLT R0, false_label119
 LDR R1, ONE
 JMP trueexit_label120
false_label119 LDR R1, ZERO
trueexit_label120 ADI R3, #0
 MOV R0, FP
 ADI R0, #-296
 STR R1, R0
 MOV R0, FP
 ADI R0, #-67
 LDR R0, R0
 LDR R1, lablit2
 CMP R0, R1
 BNZ R0, false_label121
 LDR R1, ONE
 JMP trueexit_label122
false_label121 LDR R1, ZERO
trueexit_label122 ADI R3, #0
 MOV R0, FP
 ADI R0, #-300
 STR R1, R0
 MOV R0, FP
 ADI R0, #-296
 LDR R0, R0
 MOV R1, FP
 ADI R1, #-300
 LDR R1, R1
 LDR R2, ONE
 CMP R2, R1
 BGT R2, false_label123
 CMP R0, R1
 BLT R0, false_label123
 LDR R1, ONE
 JMP trueexit_label124
false_label123 LDR R1, ZERO
trueexit_label124 ADI R3, #0
 MOV R0, FP
 ADI R0, #-304
 STR R1, R0
 MOV R0, FP
 ADI R0, #-284
 LDR R0, R0
 MOV R1, FP
 ADI R1, #-304
 LDR R1, R1
 LDR R2, ONE
 CMP R2, R1
 BRZ R2, trueexit_label126
 CMP R0, R1
 BGT R0, trueexit_label126
 LDR R1, ZERO
 JMP false_label125
trueexit_label126 LDR R1, ONE
false_label125 ADI R3, #0
 MOV R0, FP
 ADI R0, #-308
 STR R1, R0
 MOV R0, FP
 ADI R0, #-264
 LDR R0, R0
 MOV R1, FP
 ADI R1, #-308
 LDR R1, R1
 LDR R2, ONE
 CMP R2, R1
 BGT R2, false_label127
 CMP R0, R1
 BLT R0, false_label127
 LDR R1, ONE
 JMP trueexit_label128
false_label127 LDR R1, ZERO
trueexit_label128 ADI R3, #0
 MOV R0, FP
 ADI R0, #-312
 STR R1, R0
 MOV R1, FP
 ADI R1, #-312
 LDR R1, R1
 BRZ R1, if_label33
 LDR R1, lablit3
 MOV R0, FP
 ADI R0, #-40
 STR R1, R0
if_label33 ADI R3, #0
 MOV R0, FP
 ADI R0, #-40
 LDR R0, R0
 LDR R1, lablit3
 CMP R0, R1
 BNZ R0, false_label129
 LDR R1, ONE
 JMP trueexit_label130
false_label129 LDR R1, ZERO
trueexit_label130 ADI R3, #0
 MOV R0, FP
 ADI R0, #-316
 STR R1, R0
 MOV R1, FP
 ADI R1, #-316
 LDR R1, R1
 BRZ R1, if_label34
 MOV R1, FP
 ADI R1, #-8
 LDR R1, R1
 MOV R2, SP
 ADI R2, #-8
 STR R1, R2
 MOV R1, FP
 ADI R1, #-22
 LDB R1, R1
 MOV R2, SP
 ADI R2, #-9
 STR R1, R2
 MOV R1, FP
 ADI R1, #-43
 LDB R1, R1
 MOV R2, SP
 ADI R2, #-10
 STB R1, R2
 MOV R4, FP
 MOV FP, SP
 ADI SP, #-4
 STR R4, SP
 ADI SP, #-26
 MOV R5, PC
 ADI R5, #36
 STR R5, FP
 JMP Functions_printPassing
 MOV R0, FP
 ADI R0, #-320
 STR R1, R0
 MOV R0, FP
 ADI R0, #-320
 LDA R1, lablit162
output_string1 LDB R3, R1
 LDB R2, NULLTERM
 CMP R2, R3
 BRZ R2, exit_string1
 TRP #3
 ADI R1, #1
 JMP output_string1
exit_string1 ADI R3, #0
 JMP if_exitlabel35
if_label34 ADI R3, #0
 MOV R1, FP
 ADI R1, #-8
 LDR R1, R1
 MOV R2, SP
 ADI R2, #-8
 STR R1, R2
 MOV R4, FP
 MOV FP, SP
 ADI SP, #-4
 STR R4, SP
 ADI SP, #-11
 MOV R5, PC
 ADI R5, #36
 STR R5, FP
 JMP Functions_printFail
 MOV R0, FP
 ADI R0, #-324
 STR R1, R0
 MOV R0, FP
 ADI R0, #-324
if_exitlabel35 ADI R3, #0
 MOV R4, FP
 ADI R4, #-4
 MOV SP, FP
 LDR FP, R4
 LDR R5, SP
 JMR R5
Functions_fibonacciSequence ADI R3, #0
 MOV R2, FP
 ADI R2, #-37
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-38
 LDR R1, ZERO
 STB R1, R2
 MOV R2, FP
 ADI R2, #-39
 LDR R1, ZERO
 STB R1, R2
 MOV R2, FP
 ADI R2, #-43
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-47
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-51
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-55
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-59
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-63
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-67
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-71
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-75
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-79
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-83
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-87
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-91
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-95
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-99
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-103
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-107
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-111
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-115
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-119
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-123
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-127
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-131
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-135
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-139
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-143
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-147
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-151
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-155
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-159
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-163
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-167
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-171
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-175
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-179
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-183
 LDR R1, ZERO
 STR R1, R2
 MOV R1, FP
 ADI R1, #-12
 LDR R1, R1
 MOV R0, FP
 ADI R0, #-37
 STR R1, R0
 LDB R1, lablit0
 MOV R0, FP
 ADI R0, #-38
 STB R1, R0
 LDB R1, lablit1
 MOV R0, FP
 ADI R0, #-39
 STB R1, R0
 MOV R0, FP
 ADI R0, #-12
 LDR R0, R0
 LDR R1, lablit2
 CMP R0, R1
 BNZ R0, false_label0
 LDR R1, ONE
 JMP trueexit_label1
false_label0 LDR R1, ZERO
trueexit_label1 ADI R3, #0
 MOV R0, FP
 ADI R0, #-43
 STR R1, R0
 MOV R1, FP
 ADI R1, #-43
 LDR R1, R1
 BRZ R1, if_label0
 MOV R1, FP
 ADI R1, #-32
 LDR R1, R1
 MOV R4, FP
 ADI R4, #-4
 MOV SP, FP
 LDR FP, R4
 LDR R5, SP
 STR R1, SP
 JMR R5
if_label0 ADI R3, #0
 MOV R0, FP
 ADI R0, #-16
 LDR R0, R0
 LDR R1, lablit3
 CMP R0, R1
 BLT R0, trueexit_label3
 LDR R1, ZERO
 JMP false_label2
trueexit_label3 LDR R1, ONE
false_label2 ADI R3, #0
 MOV R0, FP
 ADI R0, #-47
 STR R1, R0
 MOV R1, FP
 ADI R1, #-47
 LDR R1, R1
 BRZ R1, if_label4
 MOV R1, FP
 ADI R1, #-16
 LDR R1, R1
 MOV R3, R1
 TRP #1
 JMP if_exitlabel5
if_label4 ADI R3, #0
 MOV R0, FP
 ADI R0, #-16
 LDR R0, R0
 LDR R1, lablit4
 CMP R0, R1
 BLT R0, trueexit_label5
 LDR R1, ZERO
 JMP false_label4
trueexit_label5 LDR R1, ONE
false_label4 ADI R3, #0
 MOV R0, FP
 ADI R0, #-51
 STR R1, R0
 MOV R1, FP
 ADI R1, #-51
 LDR R1, R1
 BRZ R1, if_label2
 LDR R1, lablit2
 MOV R0, FP
 ADI R0, #-20
 STR R1, R0
 MOV R1, FP
 ADI R1, #-16
 LDR R1, R1
 MOV R0, FP
 ADI R0, #-24
 STR R1, R0
 MOV R1, FP
 ADI R1, #-24
 LDR R1, R1
 MOV R3, R1
 TRP #1
 JMP if_exitlabel3
if_label2 ADI R3, #0
 LDR R0, lablit2
 LDR R1, lablit3
 CMP R0, R1
 BNZ R0, false_label6
 LDR R1, ONE
 JMP trueexit_label7
false_label6 LDR R1, ZERO
trueexit_label7 ADI R3, #0
 MOV R0, FP
 ADI R0, #-55
 STR R1, R0
 MOV R1, FP
 ADI R1, #-55
 LDR R1, R1
 BRZ R1, if_label1
 LDR R0, ZERO
 MOV R1, SP
 ADI R1, #-8
 STR R0, R1
 MOV R4, FP
 MOV FP, SP
 ADI SP, #-4
 STR R4, SP
 ADI SP, #-11
 MOV R5, PC
 ADI R5, #36
 STR R5, FP
 JMP Functions_printFail
 MOV R0, FP
 ADI R0, #-59
 STR R1, R0
 MOV R0, FP
 ADI R0, #-59
if_label1 ADI R3, #0
 MOV R0, FP
 ADI R0, #-20
 LDR R0, R0
 MOV R1, FP
 ADI R1, #-24
 LDR R1, R1
 ADD R1, R0
 MOV R0, FP
 ADI R0, #-63
 STR R1, R0
 MOV R1, FP
 ADI R1, #-63
 LDR R1, R1
 MOV R0, FP
 ADI R0, #-28
 STR R1, R0
 MOV R1, FP
 ADI R1, #-24
 LDR R1, R1
 MOV R0, FP
 ADI R0, #-20
 STR R1, R0
 MOV R1, FP
 ADI R1, #-28
 LDR R1, R1
 MOV R0, FP
 ADI R0, #-24
 STR R1, R0
 MOV R1, FP
 ADI R1, #-28
 LDR R1, R1
 MOV R3, R1
 TRP #1
if_exitlabel3 ADI R3, #0
if_exitlabel5 ADI R3, #0
 MOV R0, FP
 ADI R0, #-37
 LDR R0, R0
 LDR R1, lablit3
 SUB R0, R1
 MOV R1, R0
 MOV R0, FP
 ADI R0, #-67
 STR R1, R0
 MOV R0, FP
 ADI R0, #-16
 LDR R0, R0
 MOV R1, FP
 ADI R1, #-67
 LDR R1, R1
 CMP R0, R1
 BRZ R0, false_label8
 LDR R1, ONE
 JMP trueexit_label9
false_label8 LDR R1, ZERO
trueexit_label9 ADI R3, #0
 MOV R0, FP
 ADI R0, #-71
 STR R1, R0
 MOV R1, FP
 ADI R1, #-71
 LDR R1, R1
 BRZ R1, if_label11
 MOV R1, FP
 ADI R1, #-38
 LDB R1, R1
 MOV R3, R1
 TRP #3
 MOV R1, FP
 ADI R1, #-39
 LDB R1, R1
 MOV R3, R1
 TRP #3
 JMP if_exitlabel12
if_label11 ADI R3, #0
 LDR R0, lablit3
 LDR R1, lablit3
 CMP R0, R1
 BNZ R0, false_label10
 LDR R1, ONE
 JMP trueexit_label11
false_label10 LDR R1, ZERO
trueexit_label11 ADI R3, #0
 MOV R0, FP
 ADI R0, #-75
 STR R1, R0
 MOV R1, FP
 ADI R1, #-75
 LDR R1, R1
 BRZ R1, if_label10
 LDR R0, lablit3
 LDR R1, lablit3
 CMP R0, R1
 BNZ R0, false_label12
 LDR R1, ONE
 JMP trueexit_label13
false_label12 LDR R1, ZERO
trueexit_label13 ADI R3, #0
 MOV R0, FP
 ADI R0, #-79
 STR R1, R0
 LDR R0, lablit2
 LDR R1, lablit2
 CMP R0, R1
 BNZ R0, false_label14
 LDR R1, ONE
 JMP trueexit_label15
false_label14 LDR R1, ZERO
trueexit_label15 ADI R3, #0
 MOV R0, FP
 ADI R0, #-83
 STR R1, R0
 MOV R0, FP
 ADI R0, #-79
 LDR R0, R0
 MOV R1, FP
 ADI R1, #-83
 LDR R1, R1
 LDR R2, ONE
 CMP R2, R1
 BGT R2, false_label16
 CMP R0, R1
 BLT R0, false_label16
 LDR R1, ONE
 JMP trueexit_label17
false_label16 LDR R1, ZERO
trueexit_label17 ADI R3, #0
 MOV R0, FP
 ADI R0, #-87
 STR R1, R0
 MOV R1, FP
 ADI R1, #-87
 LDR R1, R1
 BRZ R1, if_label9
 MOV R0, FP
 ADI R0, #-33
 LDB R0, R0
 LDB R1, lablit15
 CMP R0, R1
 BRZ R0, false_label18
 LDR R1, ONE
 JMP trueexit_label19
false_label18 LDR R1, ZERO
trueexit_label19 ADI R3, #0
 MOV R0, FP
 ADI R0, #-91
 STB R1, R0
 MOV R1, FP
 ADI R1, #-91
 LDR R1, R1
 BRZ R1, if_label7
 LDR R0, ZERO
 MOV R1, SP
 ADI R1, #-8
 STR R0, R1
 MOV R4, FP
 MOV FP, SP
 ADI SP, #-4
 STR R4, SP
 ADI SP, #-11
 MOV R5, PC
 ADI R5, #36
 STR R5, FP
 JMP Functions_printFail
 MOV R0, FP
 ADI R0, #-95
 STR R1, R0
 MOV R0, FP
 ADI R0, #-95
 JMP if_exitlabel8
if_label7 ADI R3, #0
 MOV R0, FP
 ADI R0, #-37
 LDR R0, R0
 LDR R1, lablit3
 CMP R0, R1
 BNZ R0, false_label20
 LDR R1, ONE
 JMP trueexit_label21
false_label20 LDR R1, ZERO
trueexit_label21 ADI R3, #0
 MOV R0, FP
 ADI R0, #-99
 STR R1, R0
 MOV R0, FP
 ADI R0, #-28
 LDR R0, R0
 LDR R1, lablit2
 CMP R0, R1
 BNZ R0, false_label22
 LDR R1, ONE
 JMP trueexit_label23
false_label22 LDR R1, ZERO
trueexit_label23 ADI R3, #0
 MOV R0, FP
 ADI R0, #-103
 STR R1, R0
 MOV R0, FP
 ADI R0, #-99
 LDR R0, R0
 MOV R1, FP
 ADI R1, #-103
 LDR R1, R1
 LDR R2, ONE
 CMP R2, R1
 BGT R2, false_label24
 CMP R0, R1
 BLT R0, false_label24
 LDR R1, ONE
 JMP trueexit_label25
false_label24 LDR R1, ZERO
trueexit_label25 ADI R3, #0
 MOV R0, FP
 ADI R0, #-107
 STR R1, R0
 MOV R0, FP
 ADI R0, #-37
 LDR R0, R0
 LDR R1, lablit18
 CMP R0, R1
 BNZ R0, false_label26
 LDR R1, ONE
 JMP trueexit_label27
false_label26 LDR R1, ZERO
trueexit_label27 ADI R3, #0
 MOV R0, FP
 ADI R0, #-111
 STR R1, R0
 MOV R0, FP
 ADI R0, #-28
 LDR R0, R0
 LDR R1, lablit19
 CMP R0, R1
 BNZ R0, false_label28
 LDR R1, ONE
 JMP trueexit_label29
false_label28 LDR R1, ZERO
trueexit_label29 ADI R3, #0
 MOV R0, FP
 ADI R0, #-115
 STR R1, R0
 MOV R0, FP
 ADI R0, #-111
 LDR R0, R0
 MOV R1, FP
 ADI R1, #-115
 LDR R1, R1
 LDR R2, ONE
 CMP R2, R1
 BGT R2, false_label30
 CMP R0, R1
 BLT R0, false_label30
 LDR R1, ONE
 JMP trueexit_label31
false_label30 LDR R1, ZERO
trueexit_label31 ADI R3, #0
 MOV R0, FP
 ADI R0, #-119
 STR R1, R0
 MOV R0, FP
 ADI R0, #-107
 LDR R0, R0
 MOV R1, FP
 ADI R1, #-119
 LDR R1, R1
 LDR R2, ONE
 CMP R2, R1
 BRZ R2, trueexit_label33
 CMP R0, R1
 BGT R0, trueexit_label33
 LDR R1, ZERO
 JMP false_label32
trueexit_label33 LDR R1, ONE
false_label32 ADI R3, #0
 MOV R0, FP
 ADI R0, #-123
 STR R1, R0
 MOV R0, FP
 ADI R0, #-37
 LDR R0, R0
 LDR R1, lablit20
 CMP R0, R1
 BNZ R0, false_label34
 LDR R1, ONE
 JMP trueexit_label35
false_label34 LDR R1, ZERO
trueexit_label35 ADI R3, #0
 MOV R0, FP
 ADI R0, #-127
 STR R1, R0
 MOV R0, FP
 ADI R0, #-28
 LDR R0, R0
 LDR R1, lablit21
 CMP R0, R1
 BNZ R0, false_label36
 LDR R1, ONE
 JMP trueexit_label37
false_label36 LDR R1, ZERO
trueexit_label37 ADI R3, #0
 MOV R0, FP
 ADI R0, #-131
 STR R1, R0
 MOV R0, FP
 ADI R0, #-127
 LDR R0, R0
 MOV R1, FP
 ADI R1, #-131
 LDR R1, R1
 LDR R2, ONE
 CMP R2, R1
 BGT R2, false_label38
 CMP R0, R1
 BLT R0, false_label38
 LDR R1, ONE
 JMP trueexit_label39
false_label38 LDR R1, ZERO
trueexit_label39 ADI R3, #0
 MOV R0, FP
 ADI R0, #-135
 STR R1, R0
 MOV R0, FP
 ADI R0, #-123
 LDR R0, R0
 MOV R1, FP
 ADI R1, #-135
 LDR R1, R1
 LDR R2, ONE
 CMP R2, R1
 BRZ R2, trueexit_label41
 CMP R0, R1
 BGT R0, trueexit_label41
 LDR R1, ZERO
 JMP false_label40
trueexit_label41 LDR R1, ONE
false_label40 ADI R3, #0
 MOV R0, FP
 ADI R0, #-139
 STR R1, R0
 MOV R0, FP
 ADI R0, #-37
 LDR R0, R0
 LDR R1, lablit22
 CMP R0, R1
 BNZ R0, false_label42
 LDR R1, ONE
 JMP trueexit_label43
false_label42 LDR R1, ZERO
trueexit_label43 ADI R3, #0
 MOV R0, FP
 ADI R0, #-143
 STR R1, R0
 MOV R0, FP
 ADI R0, #-28
 LDR R0, R0
 LDR R1, lablit23
 CMP R0, R1
 BNZ R0, false_label44
 LDR R1, ONE
 JMP trueexit_label45
false_label44 LDR R1, ZERO
trueexit_label45 ADI R3, #0
 MOV R0, FP
 ADI R0, #-147
 STR R1, R0
 MOV R0, FP
 ADI R0, #-143
 LDR R0, R0
 MOV R1, FP
 ADI R1, #-147
 LDR R1, R1
 LDR R2, ONE
 CMP R2, R1
 BGT R2, false_label46
 CMP R0, R1
 BLT R0, false_label46
 LDR R1, ONE
 JMP trueexit_label47
false_label46 LDR R1, ZERO
trueexit_label47 ADI R3, #0
 MOV R0, FP
 ADI R0, #-151
 STR R1, R0
 MOV R0, FP
 ADI R0, #-139
 LDR R0, R0
 MOV R1, FP
 ADI R1, #-151
 LDR R1, R1
 LDR R2, ONE
 CMP R2, R1
 BRZ R2, trueexit_label49
 CMP R0, R1
 BGT R0, trueexit_label49
 LDR R1, ZERO
 JMP false_label48
trueexit_label49 LDR R1, ONE
false_label48 ADI R3, #0
 MOV R0, FP
 ADI R0, #-155
 STR R1, R0
 MOV R0, FP
 ADI R0, #-37
 LDR R0, R0
 LDR R1, lablit24
 CMP R0, R1
 BNZ R0, false_label50
 LDR R1, ONE
 JMP trueexit_label51
false_label50 LDR R1, ZERO
trueexit_label51 ADI R3, #0
 MOV R0, FP
 ADI R0, #-159
 STR R1, R0
 MOV R0, FP
 ADI R0, #-28
 LDR R0, R0
 LDR R1, lablit25
 CMP R0, R1
 BNZ R0, false_label52
 LDR R1, ONE
 JMP trueexit_label53
false_label52 LDR R1, ZERO
trueexit_label53 ADI R3, #0
 MOV R0, FP
 ADI R0, #-163
 STR R1, R0
 MOV R0, FP
 ADI R0, #-159
 LDR R0, R0
 MOV R1, FP
 ADI R1, #-163
 LDR R1, R1
 LDR R2, ONE
 CMP R2, R1
 BGT R2, false_label54
 CMP R0, R1
 BLT R0, false_label54
 LDR R1, ONE
 JMP trueexit_label55
false_label54 LDR R1, ZERO
trueexit_label55 ADI R3, #0
 MOV R0, FP
 ADI R0, #-167
 STR R1, R0
 MOV R0, FP
 ADI R0, #-155
 LDR R0, R0
 MOV R1, FP
 ADI R1, #-167
 LDR R1, R1
 LDR R2, ONE
 CMP R2, R1
 BRZ R2, trueexit_label57
 CMP R0, R1
 BGT R0, trueexit_label57
 LDR R1, ZERO
 JMP false_label56
trueexit_label57 LDR R1, ONE
false_label56 ADI R3, #0
 MOV R0, FP
 ADI R0, #-171
 STR R1, R0
 MOV R1, FP
 ADI R1, #-171
 LDR R1, R1
 BRZ R1, if_label6
 LDR R1, lablit3
 MOV R0, FP
 ADI R0, #-32
 STR R1, R0
if_label6 ADI R3, #0
if_exitlabel8 ADI R3, #0
if_label9 ADI R3, #0
if_label10 ADI R3, #0
if_exitlabel12 ADI R3, #0
 MOV R0, FP
 ADI R0, #-16
 LDR R0, R0
 LDR R1, lablit3
 ADD R1, R0
 MOV R0, FP
 ADI R0, #-175
 STR R1, R0
 MOV R1, FP
 ADI R1, #-175
 LDR R1, R1
 MOV R0, FP
 ADI R0, #-16
 STR R1, R0
 MOV R0, FP
 ADI R0, #-16
 LDR R0, R0
 MOV R1, FP
 ADI R1, #-12
 LDR R1, R1
 CMP R0, R1
 BNZ R0, false_label58
 LDR R1, ONE
 JMP trueexit_label59
false_label58 LDR R1, ZERO
trueexit_label59 ADI R3, #0
 MOV R0, FP
 ADI R0, #-179
 STR R1, R0
 MOV R1, FP
 ADI R1, #-179
 LDR R1, R1
 BRZ R1, if_label13
 MOV R1, FP
 ADI R1, #-32
 LDR R1, R1
 MOV R4, FP
 ADI R4, #-4
 MOV SP, FP
 LDR FP, R4
 LDR R5, SP
 STR R1, SP
 JMR R5
 JMP if_exitlabel14
if_label13 ADI R3, #0
 LDR R0, ZERO
 MOV R1, SP
 ADI R1, #-8
 STR R0, R1
 MOV R1, FP
 ADI R1, #-12
 LDR R1, R1
 MOV R2, SP
 ADI R2, #-12
 STR R1, R2
 MOV R1, FP
 ADI R1, #-16
 LDR R1, R1
 MOV R2, SP
 ADI R2, #-16
 STR R1, R2
 MOV R1, FP
 ADI R1, #-20
 LDR R1, R1
 MOV R2, SP
 ADI R2, #-20
 STR R1, R2
 MOV R1, FP
 ADI R1, #-24
 LDR R1, R1
 MOV R2, SP
 ADI R2, #-24
 STR R1, R2
 MOV R1, FP
 ADI R1, #-28
 LDR R1, R1
 MOV R2, SP
 ADI R2, #-28
 STR R1, R2
 MOV R1, FP
 ADI R1, #-32
 LDR R1, R1
 MOV R2, SP
 ADI R2, #-32
 STR R1, R2
 MOV R1, FP
 ADI R1, #-33
 LDB R1, R1
 MOV R2, SP
 ADI R2, #-33
 STB R1, R2
 MOV R4, FP
 MOV FP, SP
 ADI SP, #-4
 STR R4, SP
 ADI SP, #-183
 MOV R5, PC
 ADI R5, #36
 STR R5, FP
 JMP Functions_fibonacciSequence
 LDR R1, SP
 MOV R0, FP
 ADI R0, #-183
 STR R1, R0
 MOV R0, FP
 ADI R0, #-183
 MOV R4, FP
 ADI R4, #-4
 MOV SP, FP
 LDR FP, R4
 LDR R5, SP
 STR R1, SP
 JMR R5
if_exitlabel14 ADI R3, #0
 LDR R1, lablit2
 MOV R4, FP
 ADI R4, #-4
 MOV SP, FP
 LDR FP, R4
 LDR R5, SP
 STR R1, SP
 JMR R5
Functions_printFail ADI R3, #0
 MOV R2, FP
 ADI R2, #-9
 LDR R1, ZERO
 STB R1, R2
 MOV R2, FP
 ADI R2, #-10
 LDR R1, ZERO
 STB R1, R2
 MOV R2, FP
 ADI R2, #-11
 LDR R1, ZERO
 STB R1, R2
 LDB R1, lablit29
 MOV R0, FP
 ADI R0, #-9
 STB R1, R0
 LDB R1, lablit30
 MOV R0, FP
 ADI R0, #-10
 STB R1, R0
 LDB R1, lablit15
 MOV R0, FP
 ADI R0, #-11
 STB R1, R0
 MOV R1, FP
 ADI R1, #-9
 LDB R1, R1
 MOV R3, R1
 TRP #3
 MOV R1, FP
 ADI R1, #-10
 LDB R1, R1
 MOV R3, R1
 TRP #3
 LDB R1, lablit32
 MOV R3, R1
 TRP #3
 LDB R1, lablit33
 MOV R3, R1
 TRP #3
 MOV R1, FP
 ADI R1, #-11
 LDB R1, R1
 MOV R3, R1
 TRP #3
 LDB R1, lablit34
 MOV R3, R1
 TRP #3
 LDB R1, lablit35
 MOV R3, R1
 TRP #3
 MOV R1, FP
 ADI R1, #-9
 LDB R1, R1
 MOV R3, R1
 TRP #3
 MOV R4, FP
 ADI R4, #-4
 MOV SP, FP
 LDR FP, R4
 LDR R5, SP
 JMR R5
Functions_passing ADI R3, #0
 MOV R2, FP
 ADI R2, #-11
 LDR R1, ZERO
 STB R1, R2
 MOV R2, FP
 ADI R2, #-15
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-19
 LDR R1, ZERO
 STR R1, R2
 LDR R0, ZERO
 MOV R1, SP
 ADI R1, #-8
 STR R0, R1
 LDR R1, lablit36
 MOV R2, SP
 ADI R2, #-12
 STR R1, R2
 MOV R1, FP
 ADI R1, #-9
 LDB R1, R1
 MOV R2, SP
 ADI R2, #-13
 STB R1, R2
 MOV R1, FP
 ADI R1, #-10
 LDB R1, R1
 MOV R2, SP
 ADI R2, #-14
 STB R1, R2
 MOV R4, FP
 MOV FP, SP
 ADI SP, #-4
 STR R4, SP
 ADI SP, #-27
 MOV R5, PC
 ADI R5, #36
 STR R5, FP
 JMP Functions_okayYeahButForRealPassing
 LDB R1, SP
 MOV R0, FP
 ADI R0, #-11
 STB R1, R0
 MOV R0, FP
 ADI R0, #-11
 LDB R0, R0
 LDB R1, lablit37
 CMP R0, R1
 BNZ R0, false_label60
 LDR R1, ONE
 JMP trueexit_label61
false_label60 LDR R1, ZERO
trueexit_label61 ADI R3, #0
 MOV R0, FP
 ADI R0, #-15
 STB R1, R0
 MOV R1, FP
 ADI R1, #-15
 LDR R1, R1
 BRZ R1, if_label15
 LDR R1, lablit38
 MOV R4, FP
 ADI R4, #-4
 MOV SP, FP
 LDR FP, R4
 LDR R5, SP
 STR R1, SP
 JMR R5
 JMP if_exitlabel16
if_label15 ADI R3, #0
 LDR R1, lablit3
 LDR R0, ZERO
 ADI R0, #-1
 MUL R1, R0
exit_label62 ADI R3, #0
 MOV R0, FP
 ADI R0, #-19
 STR R1, R0
 MOV R0, FP
 ADI R0, #-19
 MOV R4, FP
 ADI R4, #-4
 MOV SP, FP
 LDR FP, R4
 LDR R5, SP
 STR R1, SP
 JMR R5
if_exitlabel16 ADI R3, #0
 LDR R1, lablit2
 MOV R4, FP
 ADI R4, #-4
 MOV SP, FP
 LDR FP, R4
 LDR R5, SP
 STR R1, SP
 JMR R5
Functions_okayYeahButForRealPassing ADI R3, #0
 MOV R2, FP
 ADI R2, #-15
 LDR R1, ZERO
 STB R1, R2
 MOV R2, FP
 ADI R2, #-16
 LDR R1, ZERO
 STB R1, R2
 MOV R2, FP
 ADI R2, #-17
 LDR R1, ZERO
 STB R1, R2
 MOV R2, FP
 ADI R2, #-18
 LDR R1, ZERO
 STB R1, R2
 MOV R2, FP
 ADI R2, #-19
 LDR R1, ZERO
 STB R1, R2
 MOV R2, FP
 ADI R2, #-20
 LDR R1, ZERO
 STB R1, R2
 MOV R2, FP
 ADI R2, #-21
 LDR R1, ZERO
 STB R1, R2
 MOV R2, FP
 ADI R2, #-22
 LDR R1, ZERO
 STB R1, R2
 MOV R2, FP
 ADI R2, #-23
 LDR R1, ZERO
 STB R1, R2
 MOV R2, FP
 ADI R2, #-27
 LDR R1, ZERO
 STR R1, R2
 LDB R1, lablit1
 MOV R0, FP
 ADI R0, #-15
 STB R1, R0
 LDB R1, lablit29
 MOV R0, FP
 ADI R0, #-16
 STB R1, R0
 LDB R1, lablit43
 MOV R0, FP
 ADI R0, #-17
 STB R1, R0
 LDB R1, lablit44
 MOV R0, FP
 ADI R0, #-18
 STB R1, R0
 LDB R1, lablit45
 MOV R0, FP
 ADI R0, #-19
 STB R1, R0
 LDB R1, lablit46
 MOV R0, FP
 ADI R0, #-20
 STB R1, R0
 LDB R1, lablit30
 MOV R0, FP
 ADI R0, #-21
 STB R1, R0
 LDB R1, lablit15
 MOV R0, FP
 ADI R0, #-22
 STB R1, R0
 LDB R1, lablit49
 MOV R0, FP
 ADI R0, #-23
 STB R1, R0
 MOV R0, FP
 ADI R0, #-12
 LDR R0, R0
 LDR R1, lablit36
 CMP R0, R1
 BNZ R0, false_label63
 LDR R1, ONE
 JMP trueexit_label64
false_label63 LDR R1, ZERO
trueexit_label64 ADI R3, #0
 MOV R0, FP
 ADI R0, #-27
 STR R1, R0
 MOV R1, FP
 ADI R1, #-27
 LDR R1, R1
 BRZ R1, if_label17
 MOV R1, FP
 ADI R1, #-13
 LDB R1, R1
 MOV R3, R1
 TRP #3
 MOV R1, FP
 ADI R1, #-14
 LDB R1, R1
 MOV R3, R1
 TRP #3
 MOV R1, FP
 ADI R1, #-15
 LDB R1, R1
 MOV R3, R1
 TRP #3
 MOV R1, FP
 ADI R1, #-17
 LDB R1, R1
 MOV R3, R1
 TRP #3
 MOV R1, FP
 ADI R1, #-18
 LDB R1, R1
 MOV R3, R1
 TRP #3
 MOV R1, FP
 ADI R1, #-19
 LDB R1, R1
 MOV R3, R1
 TRP #3
 MOV R1, FP
 ADI R1, #-19
 LDB R1, R1
 MOV R3, R1
 TRP #3
 MOV R1, FP
 ADI R1, #-20
 LDB R1, R1
 MOV R3, R1
 TRP #3
 MOV R1, FP
 ADI R1, #-17
 LDB R1, R1
 MOV R3, R1
 TRP #3
 MOV R1, FP
 ADI R1, #-17
 LDB R1, R1
 MOV R3, R1
 TRP #3
 MOV R1, FP
 ADI R1, #-21
 LDB R1, R1
 MOV R3, R1
 TRP #3
 MOV R1, FP
 ADI R1, #-18
 LDB R1, R1
 MOV R3, R1
 TRP #3
 MOV R1, FP
 ADI R1, #-22
 LDB R1, R1
 MOV R3, R1
 TRP #3
 MOV R1, FP
 ADI R1, #-23
 LDB R1, R1
 MOV R3, R1
 TRP #3
 LDB R1, lablit49
 MOV R3, R1
 TRP #3
 LDB R1, lablit49
 MOV R3, R1
 TRP #3
 MOV R1, FP
 ADI R1, #-16
 LDB R1, R1
 MOV R3, R1
 TRP #3
 LDB R1, lablit37
 MOV R4, FP
 ADI R4, #-4
 MOV SP, FP
 LDR FP, R4
 LDR R5, SP
 STB R1, SP
 JMR R5
if_label17 ADI R3, #0
 LDB R1, lablit30
 MOV R4, FP
 ADI R4, #-4
 MOV SP, FP
 LDR FP, R4
 LDR R5, SP
 STB R1, SP
 JMR R5
 LDB R1, lablit55
 MOV R4, FP
 ADI R4, #-4
 MOV SP, FP
 LDR FP, R4
 LDR R5, SP
 STB R1, SP
 JMR R5
Functions_printPassing ADI R3, #0
 MOV R2, FP
 ADI R2, #-14
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-18
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-22
 LDR R1, ZERO
 STR R1, R2
 MOV R2, FP
 ADI R2, #-26
 LDR R1, ZERO
 STR R1, R2
 LDR R0, ZERO
 MOV R1, SP
 ADI R1, #-8
 STR R0, R1
 MOV R1, FP
 ADI R1, #-10
 LDB R1, R1
 MOV R2, SP
 ADI R2, #-9
 STB R1, R2
 MOV R1, FP
 ADI R1, #-9
 LDB R1, R1
 MOV R2, SP
 ADI R2, #-10
 STB R1, R2
 MOV R4, FP
 MOV FP, SP
 ADI SP, #-4
 STR R4, SP
 ADI SP, #-19
 MOV R5, PC
 ADI R5, #36
 STR R5, FP
 JMP Functions_passing
 LDR R1, SP
 MOV R0, FP
 ADI R0, #-18
 STR R1, R0
 MOV R1, FP
 ADI R1, #-18
 LDR R1, R1
 MOV R0, FP
 ADI R0, #-14
 STR R1, R0
 MOV R0, FP
 ADI R0, #-14
 LDR R0, R0
 LDR R1, lablit38
 CMP R0, R1
 BRZ R0, false_label65
 LDR R1, ONE
 JMP trueexit_label66
false_label65 LDR R1, ZERO
trueexit_label66 ADI R3, #0
 MOV R0, FP
 ADI R0, #-22
 STR R1, R0
 MOV R1, FP
 ADI R1, #-22
 LDR R1, R1
 BRZ R1, if_label18
 LDR R0, ZERO
 MOV R1, SP
 ADI R1, #-8
 STR R0, R1
 MOV R4, FP
 MOV FP, SP
 ADI SP, #-4
 STR R4, SP
 ADI SP, #-11
 MOV R5, PC
 ADI R5, #36
 STR R5, FP
 JMP Functions_printFail
 MOV R0, FP
 ADI R0, #-26
 STR R1, R0
 MOV R0, FP
 ADI R0, #-26
if_label18 ADI R3, #0
 MOV R4, FP
 ADI R4, #-4
 MOV SP, FP
 LDR FP, R4
 LDR R5, SP
 JMR R5
