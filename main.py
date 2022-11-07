from tkinter import *
from tkinter import ttk
import sys
import os 
from time import sleep
import sqlite3
from tkinter import messagebox
import PySimpleGUI as sg
import DataBase
import Servicos
import email.message
import smtplib
import keyboard

def janela_principal():
    # criação inicial
    master = Tk()
    master.title('DInformática APP')
    master.geometry('1820x980+50+10')
    master.iconbitmap('Ícone\\ico.ico')
    master.resizable(width=0,height=0)

    #FUNÇÕES GLOBAIS
    def janela2():
        master.destroy()
        master2 = Tk()
        master2.title('DInformática APP Acesso')
        master2.geometry('1820x980+50+10')
        master2.iconbitmap('Ícone\\ico.ico')
        master2.resizable(width=0,height=0)

        def sair_aplicativo():
            master2.destroy()
            sys.exit()

        def janela_valores():
            master_valores = Toplevel()
            master_valores.title('DInformática APP Valores e Códigos')
            master_valores.geometry('1820x980+50+10')
            master_valores.iconbitmap('Ícone\\ico.ico')
            master_valores.resizable(width=0,height=0)

            def botao_adicionar():
                master_valores.destroy()
                master_valores2 = Toplevel()
                master_valores2.title('DInformática APP Inserção Valores e Códigos')
                master_valores2.geometry('1820x980+50+10')
                master_valores2.iconbitmap('Ícone\\ico.ico')
                master_valores2.resizable(width=1,height=1)

                def botao_adicionar_servico():
                    Codigo = en_codigo.get()
                    Nome = en_servico.get()
                    Preco = en_preco.get()
                    Servicos.cursor.execute("""
                    INSERT INTO Servicos(Código, Nome,  Preço) VALUES(?, ?, ?)
                    """,(Codigo, Nome, Preco))
                    Servicos.conn.commit()
                    messagebox.showinfo(title='Informações de Serviço', message='Serviço Cadastrado com Sucesso!')
        
                #imagens
                img_fundo_valores2 = PhotoImage(file='Planos de Fundo\\valores2.png')
                img_botao_voltar_valores2 = PhotoImage(file='Botões\\PCadastro, PVerificar e PEditar\\2.png')
                img_botao_adicionar = PhotoImage(file='Botões\\PServiços\\Botão PServiços.png')
                img_botao_atualizar = PhotoImage(file='Botões\\P2\\Atualizar.png')

                #label
                lab_fundo_valores2 = Label(master_valores2,image=img_fundo_valores2)
                lab_fundo_valores2.pack()

                            #frame
                frame_cadastro_servicos = Frame(master_valores2,bg='#8f0001')
                frame_cadastro_servicos.place(width=1087,height=772,x=660,y=175)
                
                #barra scroll
                barralateral2 = Scrollbar(frame_cadastro_servicos,orient='vertical')
                barralateral2.pack(side=RIGHT, fill=Y)

                # texto descricao
                lista_frame2 = ttk.Treeview(frame_cadastro_servicos,height=3,columns=("col1","col2","col3","col4"))
                lista_frame2.heading('#0', text='')
                lista_frame2.heading('#1', text='Id')
                lista_frame2.heading('#2', text='Código')
                lista_frame2.heading('#3', text='Nome')
                lista_frame2.heading('#4', text='Preço')

                lista_frame2.column('#0',width=1)
                lista_frame2.column('#1',width=10)
                lista_frame2.column('#2',width=165)
                lista_frame2.column('#3',width=75)
                lista_frame2.column('#4',width=50)

                #pack lista
                lista_frame2.place(relx=0.01,rely=0.01,relwidth=0.95,relheight=0.85)
                                    
                def atualizar_pagina_servico_cadastro():
                    lista2 = Servicos.cursor.execute(""" SELECT Id, Código, Nome, Preço FROM Servicos
                        ORDER BY Id ASC""")
                    for i in lista2:
                        lista_frame2.insert("", END, values=i)

                #botoes
                bt_voltar = Button(master_valores2,bd=0,image=img_botao_voltar_valores2,command= lambda:[master_valores2.destroy(),janela_valores()],cursor="cross")
                bt_voltar.place(width=192,height=100,x=407,y=857)
                bt_adicionar = Button(master_valores2,bd=0,image=img_botao_adicionar,command= botao_adicionar_servico,cursor="cross")
                bt_adicionar.place(width=258,height=100,x=55,y=857)
                bt_atualizar_valores = Button(master_valores2,bd=0,image=img_botao_atualizar,command= atualizar_pagina_servico_cadastro,cursor="cross")
                bt_atualizar_valores.place(width=192,height=100,x=407,y=707)

                
                # tokens
                en_codigo = Entry(master_valores2,bd=2, font=('Calibri',25),justify=CENTER)
                en_codigo.place(width=468, height=63,x=63,y=240)
                en_servico = Entry(master_valores2,bd=2, font=('Calibri',25),justify=CENTER)
                en_servico.place(width=468, height=63,x=63,y=402)
                en_preco = Entry(master_valores2,bd=2, font=('Calibri',25),justify=CENTER)
                en_preco.place(width=468, height=63,x=63,y=562)
                
                #loop
                master_valores2.mainloop()
                
            def botao_voltar():
                print('a')
            def voltar_janela2():
                master_valores.destroy()

            # imagens
            img_fundo_valores = PhotoImage(file='Planos de Fundo\\valores.png')
            img_botao_voltar = PhotoImage(file='Botões\\PCadastro, PVerificar e PEditar\\2.png')
            img_botao_adicionar = PhotoImage(file='Botões\\PServiços\\Botão PServiços.png')
                
            # label fundo
            lab_fundo_valores = Label(master_valores,image=img_fundo_valores)
            lab_fundo_valores.pack()

            frame_cadastro_servicos = Frame(master_valores,bg='#8f0001')
            frame_cadastro_servicos.place(width=1087,height=772,x=660,y=175)
                
                #barra scroll
            barralateral2 = Scrollbar(frame_cadastro_servicos,orient='vertical')
            barralateral2.pack(side=RIGHT, fill=Y)

            # texto descricao
            lista_frame2 = ttk.Treeview(frame_cadastro_servicos,height=3,columns=("col1","col2","col3","col4"))
            lista_frame2.heading('#0', text='')
            lista_frame2.heading('#1', text='Id')
            lista_frame2.heading('#2', text='Código')
            lista_frame2.heading('#3', text='Nome')
            lista_frame2.heading('#4', text='Preço')

            lista_frame2.column('#0',width=1)
            lista_frame2.column('#1',width=10)
            lista_frame2.column('#2',width=165)
            lista_frame2.column('#3',width=75)
            lista_frame2.column('#4',width=50)

            #pack lista
            lista_frame2.place(relx=0.01,rely=0.01,relwidth=0.95,relheight=0.85)
                                
            lista2 = Servicos.cursor.execute(""" SELECT Id, Código, Nome, Preço FROM Servicos
                    ORDER BY Id ASC""")
            for i in lista2:
                lista_frame2.insert("", END, values=i)


            # botoes
            bt_voltar = Button(master_valores,bd=0,image=img_botao_voltar,command= lambda:[voltar_janela2()],cursor="cross")
            bt_voltar.place(width=192,height=100,x=130,y=832)
            bt_adicionar = Button(master_valores,bd=0,image=img_botao_adicionar,command= lambda:[botao_adicionar()],cursor="cross")
            bt_adicionar.place(width=258,height=100,x=110,y=325)
            #loop
            master_valores.mainloop()

        def janela_cadastro():
            master_cadastro = Toplevel()
            master_cadastro.title('DInformática APP Cadastro')
            master_cadastro.geometry('1820x980+50+10')
            master_cadastro.iconbitmap('Ícone\\ico.ico')
            master_cadastro.resizable(width=0,height=0)

            def voltar_janela2():
                master_cadastro.destroy()

            def botao_ok():
                Cliente = en_nome.get()
                Telefone = en_telefone.get()
                Email = en_email.get()
                Orcamento = en_orcamento.get()
                Descricao = texto_descricao_pedido.get("1.0","end-1c")
                Status = en_status.get()

                corpo_email = f"""
                <h1> A Serviços DInformática agradece a preferência!</h1>
                <p>Olá {Cliente} seu pedido foi realizado com sucesso!</p>
                <p>O orçamento é de {Orcamento} e o que você pediu para realizarmos foi: {Descricao}
                """


                msg = email.message.Message()
                msg['Subject'] = 'Pedido realizado na Serviços DInformática!'
                msg['From'] = 'servicosdinformatica09@gmail.com'
                msg['To'] = f'{Email}'
                password = 'dodbptxywhtuvdlu'
                msg.add_header('Content-Type', 'text/html')
                msg.set_payload(corpo_email)
                s = smtplib.SMTP('smtp.gmail.com:587')
                s.starttls()

                s.login(msg['From'], password)
                s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
                print("Orçamento enviado!")

                DataBase.cursor.execute("""
                INSERT INTO Pedidos(Cliente, Email, Telefone, Orçamento, Descrição, Status) VALUES(?, ?, ?, ?, ?, ?)
                """,(Cliente, Email, Telefone, Orcamento, Descricao, Status))
                DataBase.conn.commit()
                messagebox.showinfo(title='Informações de Pedido', message='Pedido Realizado com Sucesso!')
                master_cadastro.destroy()

            # imagens
            img_fundo_cadastro = PhotoImage(file='Planos de Fundo\\cadastros.png')
            img_botao_voltar = PhotoImage(file='Botões\\PCadastro, PVerificar e PEditar\\2.png')
            img_botao_ok = PhotoImage(file='Botões\\PCadastro, PVerificar e PEditar\\1.png')
                
            # label fundo
            lab_fundo_cadastro = Label(master_cadastro,image=img_fundo_cadastro)
            lab_fundo_cadastro.pack()
            
            #botoes
            bt_voltar = Button(master_cadastro,bd=0,image=img_botao_voltar,command= lambda:[voltar_janela2()],cursor="cross")
            bt_voltar.place(width=192,height=100,x=310,y=832)
            bt_ok = Button(master_cadastro,bd=0,image=img_botao_ok,command= lambda:[botao_ok()],cursor="cross")
            bt_ok.place(width=192,height=100,x=38,y=832)


            #entrada nome telefone email orçamento descrição
            en_nome = Entry(master_cadastro,bd=2, font=('Calibri',25),justify=CENTER)
            en_nome.place(width=468, height=63,x=36,y=231)
            en_telefone = Entry(master_cadastro,bd=2, font=('Calibri',25),justify=CENTER)
            en_telefone.place(width=468, height=63,x=36,y=384)
            en_email = Entry(master_cadastro,bd=2, font=('Calibri',25),justify=CENTER)
            en_email.place(width=468, height=63,x=36,y=538)
            en_orcamento = Entry(master_cadastro,bd=2, font=('Calibri',25),justify=CENTER)
            en_orcamento.place(width=468, height=63,x=32,y=691)
            en_status = Entry(master_cadastro,bd=2, font=('Calibri',15),justify=CENTER)
            en_status.place(width=100,height=60,x=1530,y=180)

            #frame descricao pedido
            frame_descricao_pedido = Frame(master_cadastro,bg='#85B777')
            frame_descricao_pedido.place(width=882,height=680,x=751,y=264)
            
            #barra scroll
            barralateral1 = Scrollbar(frame_descricao_pedido)
            barralateral1.pack(side=RIGHT, fill=Y)

            # texto descricao
            texto_descricao_pedido = Text(frame_descricao_pedido, font=('Calibri',25),selectbackground='#ff0000',selectforeground='black',wrap=WORD, undo=True,yscrollcommand=barralateral1.set)
            texto_descricao_pedido.place(width=865,height=680,x=0,y=0)

            #loop
            master_cadastro.mainloop()
                
        # imagens
        img_fundo2 = PhotoImage(file='Planos de Fundo\\2.png')
        img_botao_cadastro = PhotoImage(file='Botões\\P2\\Cadastro.png')
        img_botao_verificar = PhotoImage(file='Botões\\P2\\Verificar.png')
        img_botao_editar = PhotoImage(file='Botões\\P2\\Editar.png')
        img_botao_sair = PhotoImage(file='Botões\\P2\\Sair.png')
        img_botao_valores = PhotoImage(file='Botões\\P2\\Valores.png')
        img_botao_atualizar = PhotoImage(file='Botões\\P2\\Atualizar.png')

        # label fundo
        lab_fundo2 = Label(master2,image=img_fundo2)
        lab_fundo2.pack()

        #frame
        frame_pedidos_andamento = Frame(master2,bg='#8f0001')
        frame_pedidos_andamento.place(width=1087,height=772,x=660,y=175)
        
        #barra scroll
        barralateral = Scrollbar(frame_pedidos_andamento,orient='vertical')
        barralateral.pack(side=RIGHT, fill=Y)

        # texto descricao
        lista_frame = ttk.Treeview(frame_pedidos_andamento,height=3,columns=("col1","col2","col3","col4","col5"))
        lista_frame.heading('#0', text='')
        lista_frame.heading('#1', text='Id')
        lista_frame.heading('#2', text='Cliente')
        lista_frame.heading('#3', text='Orçamento')
        lista_frame.heading('#4', text='Status')
        lista_frame.heading('#5', text='Descrição')

        lista_frame.column('#0',width=1)
        lista_frame.column('#1',width=10)
        lista_frame.column('#2',width=165)
        lista_frame.column('#3',width=75)
        lista_frame.column('#4',width=50)
        lista_frame.column('#5',width=300)

        #pack lista
        lista_frame.place(relx=0.01,rely=0.01,relwidth=0.95,relheight=0.85)

        def atualizar():
            lista = DataBase.cursor.execute(""" SELECT Id, Cliente, Orçamento, Status, Descrição FROM Pedidos
                ORDER BY Id ASC""")
            for i in lista:
                lista_frame.insert("", END, values=i)

        # botoes
        bt_cadastro = Button(master2,bd=0,image=img_botao_cadastro,command= lambda:
        [janela_cadastro()],cursor="cross")
        bt_cadastro.place(width= 253, height=100,x=63,y=206)
        bt_verificar = Button(master2,bd=0,image=img_botao_verificar,cursor="cross")
        bt_verificar.place(width= 253, height=100,x=63,y=376)
        bt_editar = Button(master2,bd=0,image=img_botao_editar,cursor="cross")
        bt_editar.place(width= 253, height=100,x=63,y=560)
        bt_sair = Button(master2,bd=0,image=img_botao_sair,command= lambda:[sair_aplicativo()],cursor="cross")
        bt_sair.place(width= 253, height=100,x=63,y=747)
        bt_valores = Button(master2,bd=0,image=img_botao_valores,command= lambda: [janela_valores()],cursor="cross")
        bt_valores.place(width= 253, height=100,x=363,y=206)
        bt_atualizar = Button(master2,bd=0,image=img_botao_atualizar,command= lambda :[atualizar()],cursor="cross")
        bt_atualizar.place(width= 253, height=100,x=363,y=376)

        # loop
        master2.mainloop()

    def validar():
        if en_usuario.get() == 'admin' and en_senha.get() == 'admin':
            sg.popup('Acesso Aprovado!')
            janela2()
        else:
            sg.popup('Usuário ou Senha incorreto!')

    # variaveis globais
    esconder_senha = StringVar()

    # imagens
    img_fundo = PhotoImage(file='Planos de Fundo\\1.png')
    img_botao = PhotoImage(file='Botões\\P1\\Botão P1.png')

    # label fundo
    lab_fundo = Label(master,image=img_fundo)
    lab_fundo.pack()

    # entrada login e senha
    en_usuario = Entry(master,bd=2, font=('Calibri',35),justify=CENTER)
    en_usuario.place(width=500, height=93,x=660,y=380)
    en_senha = Entry(master,bd=2, textvariable=esconder_senha,show='*',font=('Calibri',35),justify=CENTER)
    en_senha.place(width=500, height=93,x=660,y=661)

    # botao entrar
    bt_entrar = Button(master,bd=0,image=img_botao,command= lambda:[validar()],cursor="cross")
    bt_entrar.place(width= 268, height=119,x=775,y=785)

    #loop para funcionar a pagina 
    master.mainloop()

janela_principal()