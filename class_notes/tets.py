def StringChallenge(strParam):
  lst = strParam.split()
  str_1,str_2 = lst[0],lst[1]
  alphabetic = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
  num = ['1','2','3','4','5','6','7','8','9']
  plus_val = False
  ast_val = False
  doll_val = False
  val_str = []
  for idx,val in enumerate(str_1):
    if val=='+':
      val_str.append(val)
      if str_2[idx].lower() in alphabetic:
        plus_val = True
    elif val =='$':
      val_str.append(val)
      if str_2[idx] in num:
        doll_val = True
    elif val =='*':
      val_str.append(val)
      if str_2[idx].lower() in alphabetic:
        try:
          if ''.join([str_1[idx+1],str_1[idx+3]]) =='{}':
            num_str = eval(str_1[idx+2])
            alp = str_2[idx]
            repeat = False
            for x in range(num_str):
              if str_2[idx+x]==alp:
                repeat=True
              else:
                repeat = False
            if repeat:
              ast_val=True
        except IndexError:
          if str_2[idx].lower() in alphabetic:
            try:
              if str_2[idx+1]:
                ast_val = False
            except IndexError:
              ast_val =True
  len_str = len(val_str)
  ans_lst = []
  x_ans = {'+_val':plus_val,'*_val':ast_val,'$_val':doll_val}
  for x in val_str:
    y = f'{x}_val'
    if y in x_ans:
      ans = x_ans.get(y)
      ans_lst.append(ans)

  if False in ans_lst:
    strParam = False
  else:
    strParam = True
  # code goes here
  return strParam


# print(StringChallenge("+++++* abcdehhhhhh"))



def StringChallenge(strParam):
    spl_sym = ['!','+','-','/','%','=']
    val = True
    if len(strParam)<7:
        val = False
    if len(strParam)>31:
        val = False
    if not any(char.isdigit() for char in strParam):
        val = False
    if not any(char.isupper() for char in strParam):
        val = False
    if not any(char in spl_sym for char in strParam):
        val = False
    if 'password' in strParam.lower():
        val = False
    strParam = val
    # code goes here
    return strParam

# keep this function call here 
print(StringChallenge("passWord123!!!!"))



