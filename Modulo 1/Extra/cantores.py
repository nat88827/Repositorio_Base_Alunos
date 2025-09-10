import streamlit as st
#---------------------------------------------sidebar
st.sidebar.title('SonicStar')
st.sidebar.write('Veja o clipe de algumas estrelas')

estilos=['Pop', 'Rock', 'MPB', 'Hip-Hop']
estilo = st.sidebar.selectbox('Escolha seu estilo musical:', estilos)
 
if estilo == 'Pop':
    Cantores = ['Ariana Grande', 'Michael Jackson', 'Byonce','Brunos Mars', 'Justin Bieber']

elif estilo == 'Rock':
    Cantores = ['The Beatles','Queen',"Guns N' Roses",'Nirvana']

elif estilo == 'MPB':
    Cantores = ['Djavan', 'Rita Lee', 'Legião Urbana', 'Chico Buarque']

else:
    Cantores = ['Tupac Shakur', 'Eminem', 'Kendrick Lamar', 'Drake']


Cantor = st.sidebar.selectbox('Escolha um cantor:', Cantores)


#--------------------------------------------Pricipal
st.title('SonicStar')
st.write('Bem vindo ao seu universo musical!!')

if Cantor =='Ariana Grande':
    st.video('https://www.youtube.com/watch?v=QYh6mYIJG2Y')
    st.write('A musica "7 rings" da Ariana Grande ultrapassou 1,2 bilhões de visualizações no YouTube, tornando-se um dos clipes mais assistidos da plataforma.')


elif Cantor == 'Michael Jackson':
    st.video('https://youtu.be/Zi_XLOBDo_Y?si=6gxml3JwcizTvI1q')
    st.write("Billie Jean de Michael Jackson, lançada em 1983,ultrapassou 1 bilhão de visualizações no YouTube, consolidando-se como um dos maiores sucessos da história da música pop.")

elif Cantor == 'Beyonce':
    st.video('https://youtu.be/rNM5HW13_O8?si=H5bmSgT_973NOHL6')
    st.write('Diva, da Beyoncé, é uma das músicas mais icônicas da artista, com mais de 1 bilhão de visualizações no YouTube.')

elif Cantor == 'Brunos Mars':
    st.video('https://youtu.be/LjhCEhWiKXk?si=rmL1QTXtnd2ZNJn9')
    st.write('Versão de "Just the Way You Are" de Bruno Mars, é uma das músicas mais populares do cantor, com mais de 3 bilhões de visualizações no YouTube.')

elif Cantor == 'Justin Bieber':
    st.video('https://www.youtube.com/watch?v=kffacxfA7G4')
    st.write('Baby, de Justin Bieber,com participação de Ludacris, tem mais de 2 bilhões de visualizações no YouTube.')

elif Cantor == 'The Beatles':
    st.video('https://youtu.be/NCtzkaL2t_Y?si=WxxOj39CXJbAci4O')
    st.write("Don't let me down, dos Beatles, uma das musicas mais famosas, com mais de 100 milhões de visualizações no YouTube.")

elif Cantor == 'Queen':
    st.video('https://youtu.be/HgzGwKwLmgM?si=-wBZ3-O5SXyo-Fan')
    st.write("Don't stop me now, da banda Queen, atinguiu 2 bilhões de visualizações no YouTube.")

elif Cantor == "Guns N' Roses":
    st.video('https://youtu.be/1w7OgIMMRc4?si=1XF6GdUpPY_6ALAv')
    st.write('Sweet Child O\' Mine, do Guns N\' Roses, banda de sucesso no final dos anos 1987 de 1 bilhão de visualizações no YouTube.')

elif Cantor == 'Nirvana':
    st.video('https://youtu.be/fregObNcHC8?si=RjPZtxrTfQJp0e_B')
    st.write('The man who sold the world , do Nirvana,  tem mais de 1 bilhão de visualizações no YouTube.')


elif Cantor == 'Djavan':
    st.video("https://youtu.be/2kqdlAYNEzk?si=Y1y4ECfFKoiM_NDR")
    st.write("O cantor e compositor brasileiro Djavan é conhecido por suas letras poéticas e melodias envolventes. Suas músicas, como 'Oceano', são verdadeiros clássicos da MPB, com milhões de visualizações no YouTube.")

elif Cantor == 'Rita Lee':
    st.video("https://youtu.be/L60qWVke-Sc?si=pA6k4TKt8Nqpu8Xn")
    st.write("Rita Lee, conhecida por sua carreira solo e por sua participação na banda Os Mutantes. Suas músicas, como 'Lança Perfume', são verdadeiros clássicos da MPB.")

elif Cantor == 'Legião Urbana':
    st.video("https://youtu.be/YPLQHeUSX2g?si=6drbsrKQrQGPJI4a")
    st.write("Legião Urbana, uma das bandas mais influentes do rock brasileiro, com músicas como 'Tempo Perdido', que continuam a ressoar com novas gerações.")

elif Cantor == 'Chico Buarque':
    st.video('https://youtu.be/wBfVsucRe1w?si=Wyl3RQRcq_KIAGBY')
    st.write("Chico Buarque, um dos maiores compositores da MPB, é conhecido por suas letras poéticas e engajadas. Suas músicas, como 'Construção', são verdadeiros clássicos da música brasileira.")

elif Cantor == 'Tupac Shakur':
    st.video('https://youtu.be/M8Wj6-gPY0g?si=bc4wlzPJy7GyxgIe')
    st.write('Changes, de Tupac Shakur, é uma das músicas mais icônicas do rapper, com mais de 1 bilhão de visualizações no YouTube.')

elif Cantor == 'Eminem':
    st.video('https://youtu.be/YVkUvmDQ3HY?si=TUHv2xIrT6WO74Ha')
    st.write('Without me, de Eminem, é um dos mais influêntes rappers, com mais de 1 bilhão de visualizações no YouTube.')

elif Cantor == 'Kendrick Lamar':
    st.video('https://youtu.be/tvTRZJ-4EyI?si=W-dtaTproSz9xabN')
    st.write('HUMBLE., de Kendrick Lamar, com mais de 1 bilhão de visualizações no YouTube, suas musicas abordam questões sociais e políticas, tornando-o um dos rappers mais respeitados da atualidade.')

elif Cantor == 'Drake':
    st.video('https://youtu.be/uxpDa-c-4Mc?si=jzatItqN4kNW72UH')
    st.write('Hotline Bling, de Drake, é uma das músicas mais populares do rapper canadense, com mais de 1 bilhão de visualizações no YouTube.')



