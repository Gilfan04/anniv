# ============================================================================
# ANNIVERSARY WEBSITE - GILFAN ❤️ NURUL
# STREAMLIT VERSION
# ============================================================================
# CARA MENJALANKAN:
# 1. Install streamlit:
#    pip install streamlit streamlit-extras
#
# 2. Simpan file ini sebagai:
#    app.py
#
# 3. Jalankan:
#    streamlit run app.py
#
# 4. Upload ke GitHub
#
# 5. Deploy GRATIS di:
#    https://streamlit.io/cloud
#
# ============================================================================

import streamlit as st
import time
import random

st.set_page_config(
    page_title="Happy Anniversary ❤️",
    page_icon="💐",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================================
# CSS STYLING
# ============================================================================

st.markdown(
    """
    <style>

    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@300;400;500;700&family=Great+Vibes&display=swap');

    .stApp {
        background: linear-gradient(to bottom, #f6e9da, #f9efe4);
        overflow-x: hidden;
    }

    html, body, [class*="css"] {
        font-family: 'Cormorant Garamond', serif;
    }

    .title {
        font-family: 'Great Vibes', cursive;
        text-align: center;
        font-size: 90px;
        color: #7a4b47;
        margin-top: 20px;
        animation: float 4s ease-in-out infinite;
    }

    .subtitle {
        text-align: center;
        font-size: 28px;
        color: #5c3b37;
        margin-bottom: 40px;
    }

    .paper {
        transition: all 0.5s ease;
    }

    .paper:hover {
        transform: translateY(-8px) scale(1.02);
    }

    .glass {
        background: rgba(255,255,255,0.25);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(255,255,255,0.3);
        box-shadow: 0 8px 32px rgba(0,0,0,0.15);
        border-radius: 30px;
        padding: 30px;
    }

    .paper {
        background: rgba(255,255,255,0.5);
        padding: 40px;
        border-radius: 30px;
        box-shadow: 0 10px 40px rgba(0,0,0,0.15);
        border: 1px solid #d7bfa7;
    }

    .letter {
        font-size: 28px;
        line-height: 2.2;
        color: #4d3633;
        white-space: pre-wrap;
    }

    .flower {
        position: fixed;
        top: -10px;
        animation: fall linear infinite;
        z-index: 999;
        opacity: 0.8;
    }

    @keyframes fall {
        0% {
            transform: translateY(-10vh) rotate(0deg);
        }

        100% {
            transform: translateY(110vh) rotate(360deg);
        }
    }

    @keyframes float {
        0%,100% {
            transform: translateY(0px);
        }
        50% {
            transform: translateY(-10px);
        }
    }

    .center {
        text-align: center;
    }

    .music-box {
        background: rgba(255,255,255,0.4);
        padding: 20px;
        border-radius: 20px;
        margin-top: 20px;
        margin-bottom: 30px;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# ============================================================================
# BACKGROUND MUSIC AUTOPLAY + EFFECTS
# ============================================================================

st.markdown(
    """
    <audio autoplay loop>
        <source src="https://cdn.pixabay.com/download/audio/2022/03/15/audio_c8c8a73467.mp3?filename=romantic-piano-ambient-11071.mp3" type="audio/mp3">
    </audio>
    """,
    unsafe_allow_html=True
)

# ============================================================================
# FLOWER ANIMATION
# ============================================================================

flowers_html = ""

for _ in range(40):
    left = random.randint(0, 100)
    duration = random.randint(8, 20)
    delay = random.randint(0, 10)
    size = random.randint(20, 45)

    flowers_html += f'''
    <div class="flower" style="
        left:{left}%;
        animation-duration:{duration}s;
        animation-delay:{delay}s;
        font-size:{size}px;
    ">
        🌸
    </div>
    '''

st.markdown(flowers_html, unsafe_allow_html=True)

# ============================================================================
# FLOATING HEARTS
# ============================================================================

hearts_html = ""

for _ in range(20):
    left = random.randint(0, 100)
    duration = random.randint(10, 25)
    delay = random.randint(0, 10)
    size = random.randint(15, 30)

    hearts_html += f'''
    <div class="flower" style="
        left:{left}%;
        animation-duration:{duration}s;
        animation-delay:{delay}s;
        font-size:{size}px;
        opacity:0.5;
    ">
        💖
    </div>
    '''

st.markdown(hearts_html, unsafe_allow_html=True)

# ============================================================================
# HERO SECTION
# ============================================================================

st.markdown(
    """
    <div class='glass center'>
        <div style='font-size:90px; animation: float 4s ease-in-out infinite;'>💐</div>
        <div style='font-size:28px; color:#7a4b47;'>for the prettiest girl 🌸</div>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    "<div class='title'>Happy 1st Anniversary</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='subtitle'>Satu tahun penuh cerita, tawa, tangis, dan rasa sayang yang terus tumbuh.</div>",
    unsafe_allow_html=True
)

# ============================================================================
# OPENING LOVE MESSAGE
# ============================================================================

st.write("")

st.markdown(
    """
    <div class='glass center'>
        <h1 style='font-size:65px; color:#7a4b47; font-family: Great Vibes, cursive;'>
            💌 Sebelum Membaca...
        </h1>

        <p style='font-size:30px; color:#5c3b37; line-height:2;'>
            baca ini sambil denger lagu ini ya sayang 🎵
        </p>

        <a href='https://open.spotify.com/track/1dGr1c8CrMLDpV6mPbImSI'
           target='_blank'
           style='
                text-decoration:none;
                background:#7a4b47;
                color:white;
                padding:18px 35px;
                border-radius:40px;
                font-size:24px;
                display:inline-block;
                margin-top:20px;
                box-shadow:0 10px 25px rgba(0,0,0,0.2);
           '>
           🎵 Putar Lover - Taylor Swift
        </a>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")
st.write("")

# ============================================================================
# SPOTIFY LOVER
# ============================================================================

st.markdown(
    """
    <div class='music-box'>
        <iframe style="border-radius:12px"
        src="https://open.spotify.com/embed/track/1dGr1c8CrMLDpV6mPbImSI?utm_source=generator&theme=0"
        width="100%"
        height="152"
        frameBorder="0"
        allowfullscreen=""
        allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"
        loading="lazy">
        </iframe>
    </div>
    """,
    unsafe_allow_html=True
)

# ============================================================================
# CARDS SECTION
# ============================================================================

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        """
        <div class='paper center'>
            <h1>🌹</h1>
            <h2>Bunga Untuk Kamu</h2>
            <p>Karena kamu suka bunga, seluruh halaman ini dipenuhi bunga yang jatuh khusus buat kamu.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        """
        <div class='paper center'>
            <h1>🧸</h1>
            <h2>Peluk Virtual</h2>
            <p>Kalau lagi kangen, buka halaman ini dan anggap aku lagi meluk kamu erat.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        """
        <div class='paper center'>
            <h1>✨</h1>
            <h2>365 Hari</h2>
            <p>365 hari yang penuh cerita dan semoga terus bertambah sampai seterusnya.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

st.write("")
st.write("")
st.write("")

# ============================================================================
# LETTER
# ============================================================================

letter = '''Salam sayang,
‎
‎Haiii Nurul inii akuu Gilfan, orang yang mungkin kamu gapernah kepikiran bisa ngabisin waktu satu tahun bareng, ahahahaa kalau dipikir-pikir lucu juga yaa  kita rul bisa sampai selama ini, jujur satu tahun itu emang bukan waktu yang lama, tapi waktu yang sebentar buat ngabisin waktu kita bersama. Jujur sedih dan bahagianya pasti ada aja di hubungan kita bedua ini, semakin lama semakin aku berusaha buat mahamin gimana kamu dan apa yang kamu ingin. Jujur aku belum bisa menuhin semua wishlist kamu. Tapi, percayalah aku bakal berusaha buat menuhin itu satu-persatu. Jodoh gaada yang tau dan gaada yang bisa memprediksi, aku hari ini blom tentu sama dengan aku hari esok. Tapi, yang perlu kamu tau, aku selalu sayang dan cinta sama kamu dan aku bakal terus berusaha jadi yang terbaik buat kamu. Aku tau aku bukan yang pertama ada di hati kamu, aku juga tau aku bukan orang yang sangat kamu nanti-nantikan. Aku cuman mau kamu tau, kalau banyak hal, banyak kejadian, banyak masalah atau bahkan kebahagiaan yang kamu bawa ke aku, dan aku sangat bersyukur bisa jadi pasangan kamu saat ini. Entah apa yang ada dipikiranku saat ini dan tulisan ini, tapi yang ada di otak aku saat nulis ini cuman satu sayang, dan kamu harus tau itu. Apa yang aku pikir cuman "Aku sayang sama kamu". Mungkin pikiranku terlalu sempit buat nampung perasaanku yang sangat luas ini. Entah kata-kata apalagi yang harus aku keluarin, tapi jujur aku sangat suka kalau kamu lagi tersenyum dan jadi diri kamu sendiri. Semoga kita bisa bersama terus dan saling sayang. Kalaupun kita tidak ditakdirkan bersama aku tetap bersyukur aku bisa sayang sama kamu, aku harap itu tidak terjadi dan semoga kedepannya banyak hal baik yang menimpa kita ya sayang. Semoga semua berjalan lancar dan bahagia.
‎
‎Salam hangat,
‎Gilfan'''

st.markdown(
    "<div class='title' style='font-size:70px;'>Surat Untuk Kamu 💌</div>",
    unsafe_allow_html=True
)

container = st.empty()

typed_text = ""

for char in letter:
    typed_text += char

    container.markdown(
        f"""
        <div class='paper'>
            <div class='letter'>{typed_text}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    time.sleep(0.01)

# ============================================================================
# LOVE COUNTER
# ============================================================================

st.write("")

st.markdown(
    """
    <div class='glass center'>
        <h1 style='font-size:60px;'>⏳</h1>
        <h2 style='font-size:45px; color:#7a4b47;'>365 Hari Bersama</h2>
        <p style='font-size:24px;'>dan semoga terus bertambah selamanya 💖</p>
    </div>
    """,
    unsafe_allow_html=True
)

# ============================================================================
# INTERACTIVE FLOWERS
# ============================================================================

st.write("")
st.write("")

st.markdown(
    "<div class='title' style='font-size:65px;'>Mainkan Bunganya 🌸</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='subtitle'>Klik bunga-bunga di bawah ini dan lihat kejutan kecil muncul 💖</div>",
    unsafe_allow_html=True
)

flower_cols = st.columns(8)
flowers = ['🌷','🌹','💐','🌸','🪻','🌺','🌼','🌻']

for i, flower in enumerate(flowers):
    with flower_cols[i]:
        if st.button(flower, use_container_width=True):
            messages = [
                'Aku sayang kamu lebih dari apapun 💖',
                'Kamu rumah paling nyaman 🌸',
                'Aku beruntung punya kamu 💐',
                'Jangan pergi ya cantik 🥺',
                'Semoga kita terus bersama ✨',
                'Kamu lucu banget kalau senyum 🌷'
            ]
            st.success(random.choice(messages))

# ============================================================================
# FINAL LOVE SECTION
# ============================================================================

st.write("")
st.write("")

st.markdown(
    """
    <div class='glass center'>
        <div style='font-size:80px;'>🕯️🌸💖💐</div>
        <h1 style='font-size:65px; color:#7a4b47; font-family: Great Vibes, cursive;'>
            You Are My Favorite Person
        </h1>
        <p style='font-size:28px; color:#5c3b37;'>
            Dari sekian banyak hal yang terjadi di hidup aku,
            kamu adalah salah satu hal terbaik yang pernah datang.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# ============================================================================
# ENDING
# ============================================================================

st.write("")
st.write("")
st.write("")

st.markdown(
    "<div class='title'>To Nurul, With Love 💖</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='subtitle'>Semoga website kecil ini bisa jadi salah satu kenangan manis buat kamu.</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='center' style='font-size:60px;'>🌸 💐 🌷 💖 🕯️</div>",
    unsafe_allow_html=True
)
