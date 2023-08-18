from threading import Event
from collections import deque
from random import randrange, choice
from typing import Callable

def expedition_config() -> tuple:

    def get_random_number(x:int, y:int) -> int :return randrange(x, y)

    def get_economy(x:int, y:int) -> tuple:
        return choice(['increase', 'discount']).upper(), get_random_number(x, y) / 100

    def get_propellant(warp:int) -> float:
        return warp / 100
        
    return choice([
        {"rank":"A", "name":"Thuryn", "propellant": get_propellant(25), "estimated_time": get_random_number(4, 8), "total_extraction":get_random_number(6000, 9999)},
            {"rank":"B", "name":"Invigtha", "propellant": get_propellant(20), "estimated_time": get_random_number(6, 12), "total_extraction":get_random_number(4000, 6000)},
            {"rank":"C", "name":"Ledian", "propellant": get_propellant(15), "estimated_time": get_random_number(10, 15), "total_extraction":get_random_number(3000, 4500)},
            {"rank":"D", "name":"Dracco", "propellant": get_propellant(10), "estimated_time": get_random_number(20, 48), "total_extraction":get_random_number(2500, 3500)},
            {"rank":"E", "name":"Krivian", "propellant": get_propellant(5), "estimated_time": get_random_number(28, 60), "total_extraction":get_random_number(1500, 2100)}]),\
                choice([["silicato",35.0], ["platina",48.0], ["cobalto",50.0], ["ferro",80.0], ["níquel", 85]]),\
                choice([10, 25, 40, 60, 150, 260]),\
                    choice([["Strong", get_economy(8, 16)], 
                            ["Weak", get_economy(4, 8)], 
                                ["Average", get_economy(2, 4)]])

def launch_expedition(event:Event, flux_message: deque, spaceship:dict) -> Callable[[list], Callable]:

    print(f"Expedição {spaceship['name']} classe {spaceship['rank']} iniciada.")

    def set_rock(rock:list) -> Callable[[int], Callable]:

        def set_warp(warp_jump:int) -> Callable[[list], dict]:

            def execute_trade(economy:list) -> dict:

                flux_message.appendleft({"LOG_INFO": ("expedition_core.launch_expedition", f"Extação de {rock[0]} em andamento, tempo estimado:{spaceship['estimated_time']} jornadas")})

                event.wait(spaceship["estimated_time"])

                sale:float = rock[1] * spaceship["total_extraction"]

                flux_message.appendleft({"LOG_INFO": ("expedition_core.launch_expedition", f"Extração finalizada - Minério:{rock[0]} | Valor:{rock[1]} | Total-Extração:{spaceship['total_extraction']} | Trade:{sale}")})

                distance:int = warp_jump - int(spaceship["propellant"] * warp_jump)
                
                flux_message.appendleft({"LOG_INFO": ("expedition_core.launch_expedition", f"Distância:{warp_jump * 1000} anos-luz, propulsor:{spaceship['propellant']}% recalculando salto para {distance * 1000} anos-luz")})

                event.wait(distance)

                flux_message.appendleft({"LOG_INFO": ("expedition_core.launch_expedition", f"Salto finalizado, iniciando trade...")})

                sold:int = 0
                value:float = sale * economy[1][1]
                trade:str = ""
                
                if 'INCREASE' == economy[1][0]:
                    sold = int(sale + value)
                    trade = f'Acréscimo:+{economy[1][1]}%'
                else:
                    sold = int(sale - value)
                    trade = f'Desconto:-{economy[1][1]}%'

                flux_message.appendleft({"LOG_INFO": ("expedition_core.launch_expedition", f"Trade realizado... | Economia:{economy[0]} | {trade} | {rock[0]} - venda:{sold}")})

                return {
                    'Rank': spaceship[0],
                    'Spaceship': spaceship[1],
                    'Propellant': spaceship["propellant"],
                    'Rock':rock[0],
                    'Unit_Value':rock[1],
                    'Total_Extraction':spaceship['total_extraction'], 
                    'Estimated_Time':spaceship["estimated_time"],
                    'Sale': {sale},
                    'Distance':warp_jump * 1000,
                    'Recalculated_Distance':distance * 1000, 
                    'Economy':economy[0], 
                    'Trace': trade, 
                    'Sold': sold}

            return execute_trade

        return set_warp

    return set_rock
