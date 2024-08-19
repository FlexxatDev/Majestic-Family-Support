import disnake
from disnake.ext import commands
from typing import Optional
import os
from Config import *



bot = commands.Bot(command_prefix="!", help_command=None, intents=disnake.Intents.all(), test_guilds=[1273029650464903350])

class Fraction(disnake.ui.View):
    
    def __init__(self):
        super().__init__(timeout=None)
        self.value = Optional[bool]

    @disnake.ui.button(label="Крайм", style=disnake.ButtonStyle.blurple, emoji = "👓")
    async def Crime(self, button:disnake.ui.button, inter: disnake.MessageInteraction):
        global Frac
        await inter.send("Выберите ветку контракта", view=ContractsCrime())
        self.value = True
        Frac = "Crime"
    @disnake.ui.button(label="Госс", style=disnake.ButtonStyle.blurple, emoji = "🦺")
    async def Farm(self, button:disnake.ui.button, inter: disnake.MessageInteraction):
        global Frac
        await inter.send("Выберите ветку контракта", view=ContractsFarm())
        self.value = True
        Frac = "Farm"


class ContractsFarm(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.value = Optional[bool]

    @disnake.ui.button(label="Дары моря", style=disnake.ButtonStyle.blurple, emoji = "🐳")
    async def SeaGift(self, button:disnake.ui.button, inter: disnake.MessageInteraction):
        await inter.send("Выберите тип контракта", ephemeral=True, view=SeaGifts())
        self.value = True
    @disnake.ui.button(label="Металлург", style=disnake.ButtonStyle.blurple, emoji = "⛏")
    async def Metal(self, button:disnake.ui.button, inter: disnake.MessageInteraction):
        await inter.send("Выберите тип контракта", ephemeral=True, view=Metals())
        self.value = True

class ContractsCrime(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.value = Optional[bool]

    @disnake.ui.button(label="Гровер", style=disnake.ButtonStyle.blurple, emoji = "🌱")
    async def Grover(self, button:disnake.ui.button, inter: disnake.MessageInteraction):
        await inter.send("Выберите тип контракта", ephemeral=True, view=Grovers())
        self.value = True


class ContractLogAccept(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.value = Optional[bool]

    @disnake.ui.button(label="Принять", style=disnake.ButtonStyle.green, emoji = "✅")
    async def AcceptCont(self, button:disnake.ui.button, inter: disnake.MessageInteraction):
        await inter.send(f"Контракт принят \nКто принял - {inter.user.name}/{inter.user.display_name}")
        for i in member.split():
            try:
                if choice == 1:
                    summ, comment = await Dropdown.returnsumm(self, inter)
                elif choice == 2:
                    summ, comment = await Dropdown1.returnsumm(self, inter)
                elif choice == 3:
                    summ, comment = await Dropdown2.returnsumm(self, inter)    
                static = int(i)
                File = open("File.txt", "a+")
                File.write(f"{static};{summ};{comment}\n")
                File.close()
            except:
                pass
                
        self.value = True
        self.stop()

    @disnake.ui.button(label="Отклонить", style=disnake.ButtonStyle.red, emoji = "⛔")
    async def CancelCont(self, button:disnake.ui.button, inter: disnake.MessageInteraction):
        await inter.send(f"Контракт отклонён \nКто отклонил - {inter.user.name}/{inter.user.display_name}")
        self.value = False
        self.stop()
    
class Delete(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.value = Optional[bool]

    @disnake.ui.button(label="Остановить лог", style=disnake.ButtonStyle.red, emoji = "🎈")
    async def DeleteLog(self, button:disnake.ui.button, inter: disnake.MessageInteraction):
        os.remove("File.txt")
        File = open("File.txt", "a+")
        File.write(f"staticId;amount;comment\n")
        await inter.send("Лог остановлен")
        self.value = True
        self.stop()
    
class Dropdown1(disnake.ui.StringSelect):
    def __init__(self):
        options = [
            disnake.SelectOption(label=f"1Металлургия, Выплата: {Metal1}", description="Выполни контракт что бы получить награду"),
            disnake.SelectOption(label=f"2Металлургия, Выплата: {Metal2}", description="Выполни контракт что бы получить награду"),
            disnake.SelectOption(label=f"3Металлургия, Выплата: {Metal3}", description="Выполни контракт что бы получить награду"),
            disnake.SelectOption(label=f"4Металлургия, Выплата: {Metal4}", description="Выполни контракт что бы получить награду"),
        ]
        super().__init__(
            placeholder = "MENU",
            min_values = 1,
            max_values = 1,
            options = options 
        )
    async def callback(self, inter: disnake.MessageInteraction):
        global choice
        global member
        global contract 
        choice = 2
        member = inter.user.display_name
        contract = inter.data["values"][0]
        await ContarctLog(member, contract)
        await inter.response.send_message(f"Отчет на {self.values[0]} отправлен!", ephemeral=True)
    async def returnsumm(self, inter: disnake.MessageInteraction):
        for i in contract.split():
            try:
                money = int(i)
                return(money, f"{contract}")
            except:
                pass

class Metals(disnake.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(Dropdown1())

class Dropdown2(disnake.ui.StringSelect):
    def __init__(self):
        options = [
            disnake.SelectOption(label=f"1Гровер, Выплата: {Grover1}", description="Выполни контракт что бы получить награду"),
            disnake.SelectOption(label=f"2Гровер, Выплата: {Grover2}", description="Выполни контракт что бы получить награду"),
            disnake.SelectOption(label=f"3Гровер, Выплата: {Grover3}", description="Выполни контракт что бы получить награду"),
            disnake.SelectOption(label=f"4Гровер, Выплата: {Grover4}", description="Выполни контракт что бы получить награду"),
            disnake.SelectOption(label=f"5Гровер, Выплата: {Grover5}", description="Выполни контракт что бы получить награду")
        ]
        super().__init__(
            placeholder = "MENU",
            min_values = 1,
            max_values = 1,
            options = options 
        )
    async def callback(self, inter: disnake.MessageInteraction):
        global choice
        global member 
        global contract
        choice = 3
        member = inter.user.display_name
        contract = inter.data["values"][0]
        await ContarctLog(member, contract)
        await inter.response.send_message(f"Отчет на {self.values[0]} отправлен!", ephemeral=True)
    async def returnsumm(self, inter: disnake.MessageInteraction):
         for i in contract.split():
            try:
                money = int(i)
                return(money, f"{contract}")
            except:
                pass

class Grovers(disnake.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(Dropdown2())

class Dropdown(disnake.ui.StringSelect):
    def __init__(self):
        options = [
           disnake.SelectOption(label=f"1Дары моря, Выплата: {SeaGift1}", description="Выполни контракт что бы получить награду"),
           disnake.SelectOption(label=f"2Дары моря, Выплата: {SeaGift2}", description="Выполни контракт что бы получить награду"),
           disnake.SelectOption(label=f"3Дары моря, Выплата: {SeaGift3}", description="Выполни контракт что бы получить награду"),
           disnake.SelectOption(label=f"4Дары моря, Выплата: {SeaGift4}", description="Выполни контракт что бы получить награду"),
           disnake.SelectOption(label=f"5Дары моря, Выплата: {SeaGift5}", description="Выполни контракт что бы получить награду"),
           disnake.SelectOption(label=f"6Дары моря, Выплата: {SeaGift6}", description="Выполни контракт что бы получить награду"),
           disnake.SelectOption(label=f"7Дары моря, Выплата: {SeaGift7}", description="Выполни контракт что бы получить награду"),
           disnake.SelectOption(label=f"8Дары моря, Выплата: {SeaGift8}", description="Выполни контракт что бы получить награду")
        ]
        super().__init__(
            placeholder = "MENU",
            min_values = 1,
            max_values = 1,
            options = options 
        )
    async def callback(self, inter: disnake.MessageInteraction):
        global choice 
        global member
        global contract
        choice = 1
        member = inter.user.display_name
        contract = inter.data["values"][0]
        await ContarctLog(member, contract)
        await inter.response.send_message(f"Отчет на {self.values[0]} отправлен!", ephemeral=True)
    async def returnsumm(self, inter: disnake.MessageInteraction):
        for i in contract.split():
            try:
                money = int(i)
                return(money, f"{contract}")
            except:
                pass



class SeaGifts(disnake.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(Dropdown())
    
@bot.event
async def on_ready():
    print(f"Bot {bot.user} is ready!")

async def ContarctLog(member, contract):
    view = ContractLogAccept()
    channel = bot.get_channel(log_contracts) 
    embed = disnake.Embed(
        title= "Новый лог",
        description = f"Игрок - {member}\nКонтракт - {contract}"
        
    )
    await channel.send(embed=embed, view=view)

@bot.command()
@commands.has_permissions(administrator=True)
async def reg(ctx):
    view = Fraction()
    await ctx.send(f"Привет, выбери ветку свой фамы", view=view)
    

@bot.command()
@commands.has_permissions(administrator=True)
async def log(ctx):
    view = Delete()
    await ctx.send("Отчет для выплат", file=disnake.File("File.txt"), view=view)
    


bot.run("TOKEN")
