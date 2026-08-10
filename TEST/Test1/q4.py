#Calculate the cost of painting the following building’s walls (both interior and
#exterior). You need to accept area (one wall) and cost of both interior and
#exterior wall.
#(Note: 1. Below diagram is of two joint rooms.
#2. It is upper view of building.)
a =float(input("Enter the Area of one wall : "))
ic = float(input("Enter the interior cost : "))
ec = float(input("Enter the exterior cost : "))
interior_wal = 8
exterior_wall =6
total_exterior_cost = a* exterior_wall* ec
total_interior_wal = a * interior_wal * ic
total_cost = total_exterior_cost+ total_exterior_cost
print("interior painting cost =",total_interior_wal)
print("exterior painting cost =",total_exterior_cost)
print("Total cost :",total_cost)