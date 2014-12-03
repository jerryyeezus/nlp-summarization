from math import floor
from pyrouge import Rouge155
nums = []
for i in range(0, 100):
  nums.append(i)

print floor(len(nums)*.165)

num_to_take = floor(len(nums)*.165)

print nums[0:int(num_to_take)]


r = Rouge155()
r.system_dir = "./summary"
r.model_dir = "./summaries-gold/battery-life_amazon_kindle"
r.system_filename_pattern = "battery-life.(\d+).summary"
r.model_filename_pattern = "battery-life_amazon_kindle.[A-Z].#ID#.gold"
output = r.convert_and_evaluate()
print(output)
output_dict = r.output_to_dict(output)


r.system_dir = "./summary"
r.model_dir = "./summaries-gold/room_holiday_inn_london"
r.system_filename_pattern = "hotel_service.(\d+).summary"
r.model_filename_pattern = "room_holiday_inn_london.[A-Z].#ID#.gold"
output = r.convert_and_evaluate()
print(output)
output_dict = r.output_to_dict(output)
