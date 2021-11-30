#시작
print('안녕하세요. OOO간호사 입니다.')
print(input('이름을 적어주세요 : ')+'님 안녕하세요 ') 
answer=str(input('어디 불편하신 곳이 있으신가요?(네/아니오): '))
if answer== '네':
   print('다음 질문에 답해주시길 바랍니다.')
else:
   print('당신은 건강하군요!!')
   print('프로그램을 종료합니다.')
  
#증상물어보기
diseases=['근육통, 호흡곤란, 구토, 설사']
if answer=='네':
 print(diseases)
 disease=str(input('이들 중 해당되는 질환이 있다면 입력해주세요: '))
 if disease=='근육통':
   print('독감, 만성피로 증후군, 인후염 등이 의심됩니다.')       
 elif disease=='호흡곤란':
   print('폐렴, 천식 등이 의심됩니다.')
 elif disease=='구토':
   print('식중독, 위장염 등이 의심됩니다.')
 elif disease=='설사':
   print('소화 불량, 장염 등이 의심됩니다.')
else:
 print('')
 

#질환정보설명
ill=['독감, 만성피로 증후군, 인후염, 폐렴, 천식, 식중독, 위장염, 소화 불량, 장염']
illness=str(input('더 궁금한 질환이 있습니까? 있다면 입력해주세요: '))
if illness=='독감':
   print('독감은 마스크 사용을 권장하며,특히 영유아나 노인과 같은 고위험군은 예방접종을 권장합니다.')
elif illness=='만성피로 증후군':
   print('만성피로 증후군은 일상생활에 지장을 줄 정도의 피로감인가요? 빨리 치료를 받아보세요!!')
elif illness=='인후염':
   print('인후염은 음식물을 삼킬 때 통증이 심하신가요? 빨리 안정을 취하고 물을 많이 마시도록 하세요!!')
elif illness=='폐렴':
   print('폐렴은 기침, 가래, 호흡곤란 등이 발생하며 심할 경우 피가 묻어나기도 합니다.')
elif illness=='천식':
   print('천식은 호흡곤란,기침등이 대표적인 증상이며,갑작스럽게 증상 악화가 발생합니다.')
elif illness=='식중독':
   print('식중독은 상한 음식을 먹어 구토,발열 등의 증상이 나타납니다.자극되는 음식을 피하세요!!')
elif illness=='위장염':
   print('위장염은 위염, 장염이 동시에 발생한 것입니다. 식사를 가능한 제한해주세요!')
elif illness=='소화 불량':
   print('소화 불량이 의심되시나요? 기름진 음식, 밀가루 음식을 줄여보세요!')
elif illness=='장염':
   print('장염이 의심되시나요? 장기간의 설사로 인한 수분손실을 주의해주세요!')


#병원진찰
print('')
print('-'*50)
print('안녕하세요~~상명병원입니다. 무엇을 도와드릴까요?')
list=['건강검진하기,약처방받기,예방접종받기,의사진단받기']
print(list)
treat=str(input('진료받으실 것을 골라주세요: '))
print('<%s> 는 10분만 대기해 주세요~~!' % (treat))

print('')
print('-'*50)


#마무리
price=0
if treat=='건강검진하기':
   price =40000
elif treat=='약처방받기':
   price=15000
elif treat=='예방접종받기':
   price=25000
elif treat=='의사진단받기':
   price=10000

money=int(input('진료는 잘 받으셨나요? 총 금액은 %d원입니다: ' % (price)))

if price > money:
   print('금액이 부족합니다.')
else:
   print('감사합니다. 다음에 또 오세요~')


