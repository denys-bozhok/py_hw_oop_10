# Game where u should live usual life
# Game starts when user age is 0
# And every step of cycle add 1 to user age
# We should have a bag by default = []

# On the way of life we ,might to buy : car , home , some rich stuff and it will
# add bonus to our social_status

# On the start of this game by random user get it's material_status :
#  poor , avarage , rich

# poor - 70 y.o
# avarage- 85 y.o
# rich - 90 y.o

# social_status
# poor - 10
# avarage - 15
# rich - 30

# start_capital - depended of material_status
# poor - 500
# avarage - 1000
# rich - 10000000

# When child was born it's will recieve an IQ by random : 0 - 130 (since 75)
# When user 16 yo -> he might leave from school and get a job (-13 IQ ,+1000$ (once))
# When user 23 yo -> he might to become a student in University (+35 IQ ,-1500$ (once)/ +1500$ (for rich)) (if user was poor but become an avarage -> it can't get a degree)

# every year we might to eat on : 100(user_age-0.5) , 200(user_age-0.2) , 300(user_age+0.2)

# prof : unemployed  (75-80) (at least 100 on food) ,(80-100) Redneck(user_money + 420) , (100-130)businessman(user_money + 1500)

# if user doesn't have a money -> Game over
# Every year if in random we get next values : 13 ,23 -> Game over (Suddenly player become a deadman)

# On every iterattion we should track if user age bigger than it should

# Also we should cover cases with junk-lifestyle :
# When hero is 18 years old he might begin to smoke if it will be -> we should subtrack 88 - 15 (once + 300$)
# if user_age is more than 23 it might have a chance to have a widding every year before 50
# if user decide to have a widding -> it takes 10 years from current age
# Every year after wedding user get a chance to become an alco and then it takes also 10 years (+200$ every year)

# When game stops : show history of human and it's bag  bag become an empty package

# -> Game over

# CLASSES
# Creature
# Human  -> blueprint (abstract class)
# PoorHuman / AvarageHuman / RichHuman

# JunkHarbit : Harbit (abs) , Smoke , Drink , etc ...
# By default : damage
# Custom effects : risk_of_accident , sudden_hart_attack , black_lungs(passive = - 0.8)

# JOB : WorthJob , AvarageJob , Business

# EDUCATION : PoorSchool ,AvarageSchool , BusinessSchool

# Staff  : Car , House , Phone , Computer ...

# Props
# BY DEFAULT = money , end_point , social_status , IQ , bag ,start_capital

# CUSTOM = education , isSmoke , isDrunk
