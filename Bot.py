import disnake
from disnake.ext import commands
from typing import Optional
import os
log_contracts = None #id канала в который будут приходить логиконтрактов


bot = commands.Bot(command_prefix="!", help_command=None, intents=disnake.Intents.all(), test_guilds=[1273029650464903350])

class Register(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.value = Optional[bool]

    @disnake.ui.button(label="Дары моря", style=disnake.ButtonStyle.blurple, emoji = "🐳")
    async def SeaGift(self, button:disnake.ui.button, inter: disnake.MessageInteraction):
        await inter.send("Выберите тип контракта", ephemeral=True, view=DropdownView())
        self.value = True
    @disnake.ui.button(label="Металлург", style=disnake.ButtonStyle.blurple, emoji = "⛏")
    async def Metal(self, button:disnake.ui.button, inter: disnake.MessageInteraction):
        await inter.send("Выберите тип контракта", ephemeral=True, view=DropdownView1())
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
                    summ, comment = await Dropdown.returnsumm()
                elif choice == 2:
                    summ, comment = await Dropdown1.returnsumm()
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
            disnake.SelectOption(label="1 Металлург (Выплата 25.000$)", description="Контракт доступен раз в 24 часа")
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
        choice = 2
        member = inter.user.display_name
        contract = inter.data["values"][0]
        await ContarctLog(member, contract)
        await inter.response.send_message(f"Отчет на {self.values[0]} отправлен!", ephemeral=True)
    async def returnsumm():
        return(25000, "Металлург 1 уровень")

class DropdownView1(disnake.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(Dropdown1())

class Dropdown(disnake.ui.StringSelect):
    def __init__(self):
        options = [
            disnake.SelectOption(label="1 Уровень Дары моря (Выплата 20.000$)", description="Контракт доступен раз в 2 часа")
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
        choice = 1
        member = inter.user.display_name
        contract = inter.data["values"][0]
        await ContarctLog(member, contract)
        await inter.response.send_message(f"Отчет на {self.values[0]} отправлен!", ephemeral=True)
    async def returnsumm():
        return(20000, "Дары моря 1 уровень")



class DropdownView(disnake.ui.View):
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
    view = Register()
    await ctx.send(f"Привет! Выбери контракт для отчета!", view=view)
    

@bot.command()
@commands.has_permissions(administrator=True)
async def log(ctx):
    view = Delete()
    await ctx.send("Отчет для выплат", file=disnake.File("File.txt"), view=view)
    


bot.run("TOKEN")
