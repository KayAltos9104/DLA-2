import numpy
import random as rnd
from time import gmtime, strftime

def print_str(a,b):
    print(str(a),b)
    
class Point(object):
        
    _registry={}
        
    def __init__(self ,num_globul ,coords):
        self._registry[num_globul] = {'coords' : coords}
        self.coords = coords
        self.num_globul = num_globul
        
    def add_coords(self,coords):
        self.coords.append(coords)
            
    @classmethod 
    def remove_point(self ,num_globul):
        self._registry.pop(num_globul)

rand_final=[]
random_list =[]
max=20


pore_procent = 1.3
fore_pore_volume = pore_procent/100*max*max
pore_volume=divmod(fore_pore_volume,1)[0]

field_test = numpy.zeros((max+2,max+2))
list_for_check_calculate = numpy.array([-1, 0, 1])


def rnd_list():
    for x_rand in range(max):
            for y_rand in range(max):
                random_list.append([x_rand+1,y_rand+1])
    # print_str(random_list,'random_list')
    
rnd_list()

def check_list_new():
    global check_list
    check_list = []
    for x in list_for_check_calculate:
        for y in list_for_check_calculate:
            check_list.append([x,y])
    check_list.remove([0,0])     
    check_list=numpy.array(check_list)
    # print_str(check_list, 'check_list')

check_list_new()

def new_point():
    global point_1
    point_1=Point(1 ,[[divmod(max,2)[0]+1,divmod(max,2)[0]+1]])
new_point()


def new_particle_2():
    new_particle = rnd.choice(random_list)
    rand_final.append(new_particle)
    random_list.remove(new_particle)
    global point_2
    # point_2=Point(2 ,[[1,1]])
    point_2=Point(2 ,[[new_particle[0],new_particle[1]]])
    # print(Point._registry)
    
new_particle_2()


def coords_to_field():
    field_test.fill(0)
    # print(field_test)
    for k,v in Point._registry.items():
        # print(v)#координата частицы
        # print_str(k,'номер частицы')
        # print(v['coords'])
        for i in v['coords']:
            field_test[i[0]][i[1]]=k

    # print(field_test,'field_test')  
    
coords_to_field()


def check_neighbours():    
    # print_str(Point._registry,'до проверки')
    list_for_delete=[]
            #========= Проверка соседей (начало) =========
    if len(Point._registry)==1:
        new_particle_2()        
    for coord_check in check_list:
        x=coord_check[0]
        y=coord_check[1]  
        x_2 = Point._registry[2]['coords'][0][0]
        y_2 = Point._registry[2]['coords'][0][1]
        # print(Point._registry)
        if (field_test[x_2+x][y_2+y]==1)==True:
            # print('test finished')
            point_1.add_coords(Point._registry[2]['coords'][0])
            # print('add_coords')

            field_test[x_2][y_2]=1
            point_2.remove_point(2)
            break                  
    # print_str(Point._registry,'после удаления')   

# check_neighbours()
    
    

def moving():  
    # print(field_test)
    # print_str(Point._registry,'registry_before')
    if len(Point._registry)>1:
        x_move = Point._registry[2]['coords'][0][0]
        y_move = Point._registry[2]['coords'][0][1]
        coord_moving = Point._registry[2]['coords'][0]
                    
        crit_mix_max=0
        stop_signal=0
        check_list_moving = check_list[:]
                
        # print('test_1')
        while (crit_mix_max==0 and stop_signal==0)==True:
            
            # print(step_while,'step_while')
            step_rnd = rnd.choices(check_list_moving)
            for_sum_coord=numpy.array(step_rnd[0])
            # print_str(for_sum_coord,' for_sum_coord')
            not_use=1
                            # check_list_moving.remove(step_rnd[0])
            new_coord=numpy.array(coord_moving)
            # print_str(new_coord,' new_coord')
                        
            if step_rnd==[]:
                new_coord=coord_moving
                stop_signal=1
                break
                            
            refresh_value=[]
            t=new_coord+for_sum_coord
            # print_str(t,' t')
            # print_str(max,' max')
            refresh_value.append(t.tolist())
            # print_str(refresh_value,' refresh_value')
            if ((t[0]<1 or t[1]<1
                    or t[0]>max or t[1]>max))==True:
                        not_use+=1
                                    # print(check_list_moving)
                                    # print(step_rnd)
            if (not_use==1)==True:
                                
                # field_test[x_move][y_move]=0
                                
                # field_test[refresh_value[0][0]][refresh_value[0][1]]=2
                                
                # print(str(refresh_value), ' refresh_value')
                crit_mix_max=1
                                
                point_2._registry[2] = {'coords': refresh_value}
                # print_str(Point._registry,'промежуточно')
                # print("""================================
                #       """)
                coords_to_field()
                # print('finish')
                break
            # else:
                
                # print('расчет окончен')
                # field_test[refresh_value[0][0]][refresh_value[0][1]]=1
    # else:      
                
                
start_time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
print(field_test,'field_test - before')  
len_point = 0
while len(Point._registry[1]['coords'])<pore_volume:
    check_neighbours()
    if len(Point._registry[1]['coords'])>len_point:
        print_str(Point._registry, 'Point._registry')
        len_point=len(Point._registry[1]['coords'])
        print_str(len_point,'num points')
        print_str(len_point/max/max*100,' %')
    moving()
print(field_test,'field_test - after') 
end_time = strftime("%Y-%m-%d %H:%M:%S", gmtime())

print_str(start_time,'start')
print_str(end_time,'end')
print_str(end_time-start_time,'difference')
