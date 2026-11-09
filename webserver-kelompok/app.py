
from flask import Flask, render_template_string

app = Flask(__name__)

# TEMPLATE UTAMA WEBSITE
template = """
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{{ title }} | Kelompok 6</title>

    <style>
        :root {
            --bg: #f1f5f9;
            --surface: #ffffff;
            --card: #f8fafc;
            --text: #1e293b;
            --muted: #64748b;
            --border: #e2e8f0;
            --primary: #2563eb;
            --nav: #0f172a;
        }

        body.dark {
            --bg: #0f172a;
            --surface: #1e293b;
            --card: #273449;
            --text: #f1f5f9;
            --muted: #cbd5e1;
            --border: #334155;
            --primary: #60a5fa;
            --nav: #020617;
        }

        * {
            box-sizing: border-box;
        }

        html {
            scroll-behavior: smooth;
        }

        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: var(--bg);
            color: var(--text);
            transition: background .25s, color .25s;
        }

        nav {
            background: var(--nav);
            padding: 18px;
            display: flex;
            justify-content: center;
            align-items: center;
            flex-wrap: wrap;
            gap: 10px;
        }

        nav a {
            color: #cbd5e1;
            text-decoration: none;
            padding: 10px 13px;
            border-radius: 8px;
            font-weight: bold;
            font-size: 14px;
        }

        nav a:hover, nav a.active {
            background: #2563eb;
            color: white;
        }

        .theme-button {
            background: #334155;
            color: white;
            border: none;
            border-radius: 8px;
            padding: 10px 14px;
            cursor: pointer;
            font-size: 14px;
        }

        .theme-button:hover {
            background: #475569;
        }

        main {
            max-width: 1000px;
            margin: 45px auto;
            padding: 35px;
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: 16px;
            box-shadow: 0 5px 20px #00000010;
            min-height: 350px;
        }

        h1 {
            color: var(--primary);
            margin-top: 0;
        }

        h2, h3 {
            color: var(--text);
        }

        p {
            line-height: 1.8;
            color: var(--muted);
        }

        .card {
            background: var(--card);
            border: 1px solid var(--border);
            padding: 20px;
            border-radius: 12px;
            margin-top: 18px;
        }

        .member {
            display: flex;
            align-items: center;
            gap: 18px;
            background: var(--card);
            border: 1px solid var(--border);
            padding: 18px;
            border-radius: 12px;
            margin: 14px 0;
        }

        .avatar {
            width: 68px;
            height: 68px;
            min-width: 68px;
            border-radius: 50%;
            background: #e5e7eb;
            display: flex;
            justify-content: center;
            align-items: center;
            overflow: hidden;
        }

        .avatar img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            border-radius: 50%;
        }

        .member h3 {
            margin: 0;
            font-size: 16px;
        }

        .member p {
            margin: 5px 0;
            font-size: 14px;
        }

        .role {
            display: inline-block;
            background: #dbeafe;
            color: #1d4ed8;
            padding: 5px 10px;
            border-radius: 20px;
            font-size: 12px;
            font-weight: bold;
        }

        body.dark .role {
            background: #1e3a5f;
            color: #bfdbfe;
        }

        .search {
            width: 100%;
            padding: 13px;
            margin: 10px 0;
            border: 1px solid var(--border);
            border-radius: 9px;
            background: var(--card);
            color: var(--text);
            font-size: 15px;
        }

        .action-button {
            display: inline-block;
            background: #2563eb;
            color: white;
            padding: 12px 18px;
            border-radius: 8px;
            text-decoration: none;
            border: none;
            cursor: pointer;
            margin: 5px 5px 5px 0;
        }

        .action-button:hover {
            background: #1d4ed8;
        }

        footer {
            text-align: center;
            padding: 25px;
            color: var(--muted);
        }

        #clock {
            text-align: center;
            color: var(--muted);
            font-size: 13px;
            margin-top: 15px;
        }

        #topButton {
            position: fixed;
            bottom: 22px;
            right: 22px;
            background: #2563eb;
            color: white;
            border: none;
            padding: 13px 16px;
            border-radius: 50%;
            cursor: pointer;
            display: none;
            font-size: 18px;
        }

        .empty {
            display: none;
            text-align: center;
        }

        @media print {
            nav, footer, #topButton, .no-print, #clock {
                display: none !important;
            }

            body {
                background: white;
                color: black;
            }

            main {
                box-shadow: none;
                border: none;
                margin: 0;
            }
        }

        @media (max-width: 600px) {
            nav {
                gap: 5px;
                padding: 12px;
            }

            nav a {
                font-size: 12px;
                padding: 8px;
            }

            main {
                margin: 20px 12px;
                padding: 22px;
            }

            .member {
                gap: 12px;
                padding: 13px;
            }

            .avatar {
                width: 55px;
                height: 55px;
                min-width: 55px;
            }

            .member h3 {
                font-size: 14px;
            }
        }
    </style>
</head>

<body>

<nav>
    <a href="/beranda" class="{{ 'active' if active == 'beranda' else '' }}">Beranda</a>
    <a href="/identitas" class="{{ 'active' if active == 'identitas' else '' }}">Identitas</a>
    <a href="/kelas-ti25g" class="{{ 'active' if active == 'kelas' else '' }}">Kelas TI25G</a>
    <a href="/matkul" class="{{ 'active' if active == 'matkul' else '' }}">Mata Kuliah</a>
    <a href="/kontak" class="{{ 'active' if active == 'kontak' else '' }}">Kontak</a>
    <a href="/tentang" class="{{ 'active' if active == 'tentang' else '' }}">Tentang</a>

    <button class="theme-button no-print" onclick="toggleTheme()" id="themeButton">
        🌙 Mode Gelap
    </button>
</nav>

<main>
    <h1>{{ title }}</h1>
    {{ content | safe }}

    <div id="clock"></div>

    <div class="no-print" style="margin-top:25px">
        <button class="action-button" onclick="window.print()">
            🖨 Cetak Halaman
        </button>
    </div>
</main>

<footer>
    <b>Web Server Kelompok 6</b><br>
    Universitas Nusa Putra | 2026
    <p>© 2026 Kelompok 6. All Rights Reserved.</p>
</footer>

<button id="topButton" onclick="window.scrollTo({top:0,behavior:'smooth'})">
    ↑
</button>

<script>
    // MODE GELAP DAN TERANG
    function applyTheme(theme) {
        document.body.classList.toggle('dark', theme === 'dark');
        document.getElementById('themeButton').textContent =
            theme === 'dark' ? '☀️ Mode Terang' : '🌙 Mode Gelap';
    }

    function toggleTheme() {
        const next = document.body.classList.contains('dark')
            ? 'light' : 'dark';

        localStorage.setItem('kelompok6-theme', next);
        applyTheme(next);
    }

    applyTheme(localStorage.getItem('kelompok6-theme') || 'light');

    // JAM DAN TANGGAL
    function updateClock() {
        const now = new Date();

        document.getElementById('clock').textContent =
            now.toLocaleDateString('id-ID', {
                weekday: 'long',
                day: 'numeric',
                month: 'long',
                year: 'numeric'
            }) + ' | ' +
            now.toLocaleTimeString('id-ID');
    }

    updateClock();
    setInterval(updateClock, 1000);

    // TOMBOL KEMBALI KE ATAS
    window.addEventListener('scroll', function() {
        document.getElementById('topButton').style.display =
            window.scrollY > 250 ? 'block' : 'none';
    });

    // PENCARIAN ANGGOTA DAN MAHASISWA
    const search = document.getElementById('memberSearch');

    if (search) {
        search.addEventListener('input', function() {
            const keyword = this.value.toLowerCase();
            const members = document.querySelectorAll('.member');
            let visible = 0;

            members.forEach(function(member) {
                const match = member.textContent.toLowerCase()
                    .includes(keyword);

                member.style.display = match ? 'flex' : 'none';

                if (match) visible++;
            });

            document.getElementById('emptyMessage').style.display =
                visible === 0 ? 'block' : 'none';
        });
    }
</script>

</body>
</html>
"""


def render_page(title, content, active):
    return render_template_string(
        template,
        title=title,
        content=content,
        active=active
    )


# ENDPOINT 1: BERANDA
@app.route("/")
@app.route("/beranda")
def beranda():
    content = """
    <div class="card">
        <h2>Selamat Datang di Website Kelompok 6</h2>
        <p>
            Website resmi Kelompok 6 Universitas Nusa Putra.
            Website ini dibuat sebagai proyek pembelajaran
            Pemrograman Berbasis Platform menggunakan Python Flask.
        </p>
        <a href="/identitas" class="action-button">
            Lihat Anggota Kelompok
        </a>
        <a href="/kelas-ti25g" class="action-button">
            Lihat Kelas TI25G
        </a>
        <a href="/matkul" class="action-button">
            Informasi Mata Kuliah
        </a>
    </div>

    <div class="card">
        <h3>Informasi Website</h3>
        <p>Kelompok: 6</p>
        <p>Jumlah Anggota Kelompok: 4 Orang</p>
        <p>Kelas: TI25G</p>
        <p>Universitas: Nusa Putra</p>
        <p>Framework: Python Flask</p>
    </div>
    """

    return render_page("Beranda Kelompok 6", content, "beranda")


# ENDPOINT 2: IDENTITAS KELOMPOK
@app.route("/identitas")
def identitas():
    anggota = [
        ("MUSYARAF WATTIMENA", "20250040140", "Ketua Kelompok"),
        ("NADIA HASANAH", "20250040113", "Anggota"),
        ("MUHAMMAD IBNU ZACKY", "20250040088", "Anggota"),
        ("MUHAMMAD FAUZAN ALFARESI", "20250040124", "Anggota")
    ]

    cards = ""

    for nama, nim, jabatan in anggota:
        cards += f"""
        <div class="member">
            <div class="avatar">
                <svg viewBox="0 0 24 24" width="42" height="42"
                     fill="#9ca3af">
                    <circle cx="12" cy="8" r="4"/>
                    <path d="M4 21c0-4.5 3.5-7 8-7s8 2.5 8 7z"/>
                </svg>
            </div>
            <div>
                <h3>{nama}</h3>
                <p>NIM: {nim}</p>
                <span class="role">{jabatan}</span>
            </div>
        </div>
        """

    content = f"""
    <p>Daftar anggota resmi Kelompok 6:</p>

    <input type="text" id="memberSearch"
        class="search no-print"
        placeholder="Cari nama atau NIM anggota...">

    {cards}

    <p id="emptyMessage" class="empty">
        Anggota tidak ditemukan.
    </p>

    <div class="card">
        <h3>Kelompok 6</h3>
        <p>Universitas Nusa Putra</p>
        <p>Program Studi Teknik Informatika</p>
    </div>
    """

    return render_page("Identitas Kelompok 6", content, "identitas")


# ENDPOINT 3: KELAS TI25G
@app.route("/kelas-ti25g")
def kelas_ti25g():
    mahasiswa = [
        ("ABDUL WAHAB ROHMATULLAH", "20250040181", ""),
        ("ABU NUR AL-FARUQ", "20220040223", "https://storage.googleapis.com/assets-edlink/p/thumb-56b45898ed758da85e98bc0eba24af42f3b9dad1624f6d3db991b972c0559262-img-20240723-014316-6158911707749315862.jpg"),
        ("ADAM RIFALDI", "20250040134", ""),
        ("ADINDA ANGGRAENA SAPUTRI", "20250040014", ""),
        ("AFDHAL GIAN ARKANANTA", "20250040174", ""),
        ("AHMAD DHIYA SYIHAB", "20250040107", ""),
        ("AIRIN BUDIANTI", "20250040099", ""),
        ("ARYA PRATAMA WIJAYA KUSUMA", "20250040136", ""),
        ("BERNARDUS LABA MANIKIN", "20250040143", "https://storage.googleapis.com/assets-edlink/p/thumb-2a8e76c5199313d059289882115918858fe4b6ea5ad49438aa7451b5f41af0fe-cropped-1761238347877.jpg"),
        ("DEFA DINAH ALFARIST", "20250040125", "https://storage.googleapis.com/assets-edlink/p/thumb-17dd7628094216deebaca8f21234f2e911484caa7233df3fd38cf908e79fc61a-cropped-1785319405298.jpg"),
        ("DICKY ABDULLAH UPARA", "20250040172", ""),
        ("DIMAS SANDY", "20250040026", ""),
        ("HADI ARSA WINATA", "20250040191", ""),
        ("LAMDAN HANDIKA", "20250040085", ""),
        ("MARISA OKTAVIANI", "20250040069", "https://storage.googleapis.com/assets-edlink/p/thumb-18788a9d4d21fc1681203387ab7cacd986413d93fdf620d1028b919c983e2cfe-cropped-1764570627491.jpg"),
        ("MOHAMAD HAFIDZ MAULANA SYAHPUTRA", "20250040063", ""),
        ("MOHRARIZ STYAWAN", "20250040178", "https://storage.googleapis.com/assets-edlink/p/thumb-17d8ef6fe979e105508d0e1c9a19ed83367b19cadb2b73248db3b49a127a3f8b-607cf51c469f2.jpg"),
        ("MUHAMAD DZAMAR MUNGGARAN", "20250040094", ""),
        ("MUHAMAD NABIL ARRAIHAN", "20250040105", ""),
        ("MUHAMMAD ABDUL BA’AITS AL JABAR", "20250040157", ""),
        ("MUHAMMAD FAUZAN ALFARESI", "20250040124", ""),
        ("MUHAMMAD IBNU ZACKY", "20250040088", "https://storage.googleapis.com/assets-edlink/p/thumb-89a1fd81e70f9d71648d2acee39e6fd03c9d158f9b4130f6725a59d02481ff64-img-20250918-062440-658467610418122296.jpg"),
        ("MUSYARAF WATTIMENA", "20250040140", ""),
        ("NADIA HASANAH", "20250040113", ""),
        ("NAYSHILA SALSABILA AZZAHRA", "20250040004", "https://storage.googleapis.com/assets-edlink/p/thumb-7e8b7cbaffcf5c22f1c3eb476dc8c80a941342615545af9b997a2417c59ae748-cropped-1791269557603.jpg"),
        ("NAZLA DWI ANANDA", "20250040101", ""),
        ("PAUNDRA RIZKY PRATAMA", "20250040042", ""),
        ("PRAYOGI ANANTA SADIKO", "20250040029", ""),
        ("RIZKI HARPAN MAULANA", "20250040141", ""),
        ("RIZQI ACHMAD RIFSYA", "20250040185", ""),
        ("SALWA ALAWIYAH", "20250040096", ""),
        ("SITI SALWA FITRIANI", "20250040195", ""),
        ("TRI KHOLIPIANTO RAHMATSYAH", "20250040019", ""),
        ("TRIANA SAFITRI", "20250040150", ""),
        ("WIDI AMALIA RUMAILILI", "20250040175", "")
    ]

    cards = ""

    for nama, nim, foto in mahasiswa:
        if foto:
            avatar = f"""
            <img src="{foto}" alt="Foto {nama}"
                 onerror="this.style.display='none'">
            """
        else:
            avatar = """
            <svg viewBox="0 0 24 24" width="42" height="42"
                 fill="#9ca3af">
                <circle cx="12" cy="8" r="4"/>
                <path d="M4 21c0-4.5 3.5-7 8-7s8 2.5 8 7z"/>
            </svg>
            """

        cards += f"""
        <div class="member">
            <div class="avatar">
                {avatar}
            </div>
            <div>
                <h3>{nama}</h3>
                <p>NIM: {nim}</p>
                <span class="role">Mahasiswa TI25G</span>
            </div>
        </div>
        """

    content = f"""
    <div class="card">
        <h2>Daftar Mahasiswa TI25G</h2>
        <p>Universitas Nusa Putra</p>
        <p>Program Studi Teknik Informatika</p>
        <p><b>Total Mahasiswa: {len(mahasiswa)} Orang</b></p>
    </div>

    <input type="text" id="memberSearch"
        class="search no-print"
        placeholder="Cari nama atau NIM mahasiswa...">

    {cards}

    <p id="emptyMessage" class="empty">
        Mahasiswa tidak ditemukan.
    </p>
    """

    return render_page("Daftar Kelas TI25G", content, "kelas")


# ENDPOINT 4: MATA KULIAH
@app.route("/matkul")
def matkul():
    content = """
    <div class="card">
        <h2>Identitas Mata Kuliah</h2>
        <p><b>Mata Kuliah:</b> Pemrograman Berbasis Platform</p>
        <p><b>Program Studi:</b> Teknik Informatika</p>
        <p><b>Universitas:</b> Universitas Nusa Putra</p>
        <p><b>Dosen Pengampu:</b>
        Shinta Ayuningtias, S.Kom., M.Kom</p>
        <p><b>Kelompok:</b> 6</p>
        <p><b>Kelas:</b> TI25G</p>
        <p><b>Tahun:</b> 2026</p>
    </div>

    <div class="card">
        <h3>Tujuan Pembelajaran</h3>
        <p>
            Mempelajari konsep pemrograman berbasis platform,
            pengembangan aplikasi, serta penerapan teknologi
            dalam membangun perangkat lunak.
        </p>
    </div>
    """

    return render_page("Informasi Mata Kuliah", content, "matkul")


# ENDPOINT 5: KONTAK
@app.route("/kontak")
def kontak():
    content = """
    <div class="card">
        <h2>Informasi Kelompok</h2>
        <p><b>Kelompok:</b> 6</p>
        <p><b>Kelas:</b> TI25G</p>
        <p><b>Universitas:</b> Universitas Nusa Putra</p>
        <p><b>Program Studi:</b> Teknik Informatika</p>
    </div>

    <div class="card">
        <h3>Ketua Kelompok</h3>
        <p>Musyaraf Wattimena</p>
        <p>NIM: 20250040140</p>
    </div>

    <div class="card">
        <h3>Informasi</h3>
        <p>
            Untuk keperluan komunikasi kelompok,
            silakan menghubungi anggota kelompok secara langsung.
        </p>
    </div>
    """

    return render_page("Kontak Kelompok 6", content, "kontak")


# ENDPOINT 6: TENTANG
@app.route("/tentang")
def tentang():
    content = """
    <div class="card">
        <h2>Tentang Website</h2>
        <p>
            Website ini merupakan proyek tugas Kelompok 6
            Universitas Nusa Putra untuk mata kuliah
            Pemrograman Berbasis Platform.
        </p>
    </div>

    <div class="card">
        <h3>Teknologi yang Digunakan</h3>
        <p>Python 3.12</p>
        <p>Flask 3.1.3</p>
        <p>HTML5</p>
        <p>CSS3</p>
        <p>JavaScript</p>
    </div>

    <div class="card">
        <h3>Fitur Website</h3>
        <p>Mode gelap dan terang</p>
        <p>Pencarian anggota kelompok dan mahasiswa</p>
        <p>Navigasi responsif</p>
        <p>Jam dan tanggal otomatis</p>
        <p>Cetak halaman</p>
        <p>Tombol kembali ke atas</p>
        <p>Daftar mahasiswa kelas TI25G</p>
    </div>
    """

    return render_page("Tentang Website", content, "tentang")


# HALAMAN 404
@app.errorhandler(404)
def page_not_found(error):
    content = """
    <div class="card">
        <h2>404 - Halaman Tidak Ditemukan</h2>
        <p>Maaf, halaman yang kamu cari tidak tersedia.</p>
        <a href="/beranda" class="action-button">
            Kembali ke Beranda
        </a>
    </div>
    """

    return render_page("Halaman Tidak Ditemukan", content, ""), 404


# MENJALANKAN SERVER
if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )
