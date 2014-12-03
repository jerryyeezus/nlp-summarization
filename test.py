from pyrouge import Rouge155

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
