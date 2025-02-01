下記は、HTML と JavaScript を含む完全な Markdown ファイルの内容です。  
この内容をそのまま `setup.md` という名前で保存してください。  
※ 注意:

- Markdown ビューアによっては HTML やスクリプトが動作しない場合があります。
- コピー用ボタンの動作は、ブラウザ上で HTML と JavaScript が有効な場合にのみ機能します。

---

<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <title>Docker で GUI アプリを利用するためのセットアップ手順</title>
  <style>
    /* コードブロックのコピー用ボタン用スタイル */
    .code-container {
      position: relative;
    }
    .copy-button {
      position: absolute;
      top: 0.25em;
      right: 0.25em;
      padding: 0.2em 0.5em;
      background: #ddd;
      border: none;
      border-radius: 3px;
      cursor: pointer;
      font-size: 0.9em;
    }
    pre {
      overflow: auto;
    }
  </style>
</head>
<body>

<h1>Docker で GUI アプリを利用するためのセットアップ手順</h1>

<p>
このドキュメントでは、Docker コンテナ内で X11 アプリ（例: <code>xclock</code> や OpenCV の <code>cv.imshow</code>）を動作させ、ホスト側の X サーバ（Mac では XQuartz、Ubuntu では標準の X サーバ）にディスプレイ出力するための手順と、よく起こる問題点の対策についてまとめています。
</p>

<ul>
  <li><a href="#目次">目次</a></li>
  <li><a href="#1-前提条件と基本ファイル">1. 前提条件と基本ファイル</a>
    <ul>
      <li><a href="#11-dockerfile-の例">1.1 Dockerfile の例</a></li>
      <li><a href="#12-requirementstxt-の例">1.2 requirements.txt の例</a></li>
    </ul>
  </li>
  <li><a href="#2-mac-用の手順">2. Mac 用の手順</a>
    <ul>
      <li><a href="#21-ホスト側の設定-mac">2.1 ホスト側の設定 (Mac)</a></li>
      <li><a href="#22-docker-コンテナの設定-mac">2.2 Docker コンテナの設定 (Mac)</a></li>
      <li><a href="#23-コンテナ内での確認-mac">2.3 コンテナ内での確認 (Mac)</a></li>
    </ul>
  </li>
  <li><a href="#3-ubuntu-用の手順">3. Ubuntu 用の手順</a>
    <ul>
      <li><a href="#31-ホスト側の設定-ubuntu">3.1 ホスト側の設定 (Ubuntu)</a></li>
      <li><a href="#32-docker-コンテナの設定-ubuntu">3.2 Docker コンテナの設定 (Ubuntu)</a></li>
      <li><a href="#33-コンテナ内での確認-ubuntu">3.3 コンテナ内での確認 (Ubuntu)</a></li>
    </ul>
  </li>
  <li><a href="#4-よくある問題と対策">4. よくある問題と対策</a>
    <ul>
      <li><a href="#41-x11-接続エラー-xclock-エラー">4.1 X11 接続エラー (xclock エラー)</a></li>
      <li><a href="#42-opencv-の-cvimshow-が動作しない">4.2 OpenCV の cv.imshow が動作しない</a></li>
    </ul>
  </li>
  <li><a href="#5-参考情報補足">5. 参考情報・補足</a></li>
</ul>

<hr>

<h2 id="目次">目次</h2>

<ol>
  <li><a href="#1-前提条件と基本ファイル">前提条件と基本ファイル</a></li>
  <li><a href="#2-mac-用の手順">Mac 用の手順</a></li>
  <li><a href="#3-ubuntu-用の手順">Ubuntu 用の手順</a></li>
  <li><a href="#4-よくある問題と対策">よくある問題と対策</a></li>
  <li><a href="#5-参考情報補足">参考情報・補足</a></li>
</ol>

<hr>

<h2 id="1-前提条件と基本ファイル">1. 前提条件と基本ファイル</h2>

<h3 id="11-dockerfile-の例">1.1 Dockerfile の例</h3>

<p>
GUI 表示（<code>cv.imshow</code> 等）を利用する場合は、<code>opencv-python</code> を使用し、必要なシステムライブラリ（例: <code>libgtk2.0-dev</code>）もインストールする必要があります。以下はその例です。
</p>

<div class="code-container">
  <button class="copy-button" onclick="copyCode(this)">Copy</button>
  <pre><code class="language-docker">
FROM python:3.11-slim

WORKDIR /app

# 必要なシステムライブラリをインストール

RUN apt-get update && apt-get install -y --no-install-recommends \
 vim \
 libgl1-mesa-glx \
 libglib2.0-0 \
 libsm6 \
 libxext6 \
 libgtk2.0-dev \
 libxrender1 \
 x11-apps \
 xvfb \
 && apt-get clean && rm -rf /var/lib/apt/lists/\*

# requirements.txt をコピーして Python パッケージをインストール

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションのソースコードをコピー

COPY . /app

CMD ["bash"]
</code></pre>

</div>

<h3 id="12-requirementstxt-の例">1.2 requirements.txt の例</h3>

<p>
GUI 表示を利用する場合は、<code>opencv-python</code> のみを有効にしてください。もしヘッドレスモードで動作させるなら、<code>opencv-python-headless</code> のみを使用します。
</p>

<div class="code-container">
  <button class="copy-button" onclick="copyCode(this)">Copy</button>
  <pre><code class="language-text">
numpy
pandas
matplotlib
scikit-learn==1.5.2
tensorflow==2.18
opencv-python
# opencv-python-headless  ← GUI を利用する場合は不要
  </code></pre>
</div>

<blockquote>
<p><strong>注意:</strong> 同じプロジェクト内で <code>opencv-python</code> と <code>opencv-python-headless</code> を同時に指定すると依存関係が競合するため、用途に合わせどちらか一方を使用してください。</p>
</blockquote>

<hr>

<h2 id="2-mac-用の手順">2. Mac 用の手順</h2>

<h3 id="21-ホスト側の設定-mac">2.1 ホスト側の設定 (Mac)</h3>

<ol>
  <li>
    <p><strong>XQuartz のインストール</strong><br>
       Homebrew を使ってインストールする場合：</p>
    <div class="code-container">
      <button class="copy-button" onclick="copyCode(this)">Copy</button>
      <pre><code class="language-sh">
brew install --cask xquartz
      </code></pre>
    </div>
  </li>
  <li>
    <p><strong>XQuartz の起動と設定</strong></p>
    <ul>
      <li>
        <p>XQuartz を起動する：</p>
        <div class="code-container">
          <button class="copy-button" onclick="copyCode(this)">Copy</button>
          <pre><code class="language-sh">
open -a XQuartz
          </code></pre>
        </div>
      </li>
      <li>
        <p>
          XQuartz のメニューから <strong>Preferences → Security</strong> タブを開き、「Allow connections from network clients」にチェックを入れる。  
          ※ 設定変更後、XQuartz を再起動してください。
        </p>
      </li>
    </ul>
  </li>
  <li>
    <p><strong>xhost による接続許可</strong><br>
       Mac のターミナルで以下を実行して、外部（Docker）からの接続を許可します：</p>
    <div class="code-container">
      <button class="copy-button" onclick="copyCode(this)">Copy</button>
      <pre><code class="language-sh">
xhost +local:
      </code></pre>
    </div>
  </li>
  <li>
    <p><strong>ホスト側の DISPLAY 設定</strong><br>
       通常、Mac 側では <code>DISPLAY</code> は <code>:0</code> となりますが、Docker コンテナ内に渡すためには、環境変数として <code>DISPLAY=host.docker.internal:0</code> を使用します。  
       ※ Mac ターミナルで <code>export DISPLAY=$(ipconfig getifaddr en0):0</code> などと設定する場合もありますが、<strong>Docker 側には <code>host.docker.internal:0</code> を設定</strong>するのが推奨です。</p>
  </li>
</ol>

<h3 id="22-docker-コンテナの設定-mac">2.2 Docker コンテナの設定 (Mac)</h3>

<p>以下は Docker Compose の例です。<br>
<strong>重要:</strong> Docker Desktop for Mac では <code>network_mode: "host"</code> は使用せず、DISPLAY を <code>host.docker.internal:0</code> に設定します。</p>

<div class="code-container">
  <button class="copy-button" onclick="copyCode(this)">Copy</button>
  <pre><code class="language-yaml">
version: "3"
services:
  kaggle:
    build:
      context: .
      dockerfile: Dockerfile
    container_name: kaggle
    volumes:
      - ./src:/app/src
      # 必要に応じて X11 ソケットの共有（必須ではありません）
      - /tmp/.X11-unix:/tmp/.X11-unix
    environment:
      - PYTHONUNBUFFERED=1
      - DISPLAY=host.docker.internal:0
    tty: true
    stdin_open: true
    command: ["bash"]
  </code></pre>
</div>

<h3 id="23-コンテナ内での確認-mac">2.3 コンテナ内での確認 (Mac)</h3>

<ol>
  <li>
    <p>コンテナを起動し、シェルに入ります：</p>
    <div class="code-container">
      <button class="copy-button" onclick="copyCode(this)">Copy</button>
      <pre><code class="language-sh">
docker-compose up -d
docker exec -it kaggle bash
      </code></pre>
    </div>
  </li>
  <li>
    <p>コンテナ内で環境変数 <code>DISPLAY</code> が正しくセットされているか確認：</p>
    <div class="code-container">
      <button class="copy-button" onclick="copyCode(this)">Copy</button>
      <pre><code class="language-sh">
echo $DISPLAY
      </code></pre>
    </div>
    <p><strong>期待値:</strong> <code>host.docker.internal:0</code></p>
  </li>
  <li>
    <p>X11 アプリ（例: <code>xclock</code>）を起動して確認：</p>
    <div class="code-container">
      <button class="copy-button" onclick="copyCode(this)">Copy</button>
      <pre><code class="language-sh">
xclock
      </code></pre>
    </div>
    <p>→ Mac の画面上に時計ウィンドウが表示されれば成功です。</p>
  </li>
  <li>
    <p>OpenCV を用いたアプリ（例: <code>python image.py</code>）で <code>cv.imshow</code> を呼び出し、ウィンドウ表示を確認します。</p>
  </li>
</ol>

<hr>

<h2 id="3-ubuntu-用の手順">3. Ubuntu 用の手順</h2>

<h3 id="31-ホスト側の設定-ubuntu">3.1 ホスト側の設定 (Ubuntu)</h3>

<ol>
  <li>
    <p><strong>X サーバの確認</strong><br>
       Ubuntu では通常、X サーバ（Xorg）が起動しているので、以下で確認します：</p>
    <div class="code-container">
      <button class="copy-button" onclick="copyCode(this)">Copy</button>
      <pre><code class="language-sh">
echo $DISPLAY
      </code></pre>
    </div>
    <p><strong>期待値:</strong> <code>:0</code> または同様の値</p>
  </li>
  <li>
    <p><strong>xhost による接続許可</strong><br>
       ホストのターミナルで以下を実行し、ローカル接続を許可します：</p>
    <div class="code-container">
      <button class="copy-button" onclick="copyCode(this)">Copy</button>
      <pre><code class="language-sh">
xhost +local:
      </code></pre>
    </div>
  </li>
</ol>

<h3 id="32-docker-コンテナの設定-ubuntu">3.2 Docker コンテナの設定 (Ubuntu)</h3>

<p>Docker コンテナ起動時に、ホストの DISPLAY と X11 ソケットをコンテナに渡します。</p>

<p><strong>docker run の例:</strong></p>

<div class="code-container">
  <button class="copy-button" onclick="copyCode(this)">Copy</button>
  <pre><code class="language-sh">
docker run -it \
  -e DISPLAY=$DISPLAY \
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  your-docker-image bash
  </code></pre>
</div>

<p><strong>docker-compose.yml の例:</strong></p>

<div class="code-container">
  <button class="copy-button" onclick="copyCode(this)">Copy</button>
  <pre><code class="language-yaml">
version: "3"
services:
  kaggle:
    build:
      context: .
      dockerfile: Dockerfile
    container_name: kaggle
    volumes:
      - ./src:/app/src
      - /tmp/.X11-unix:/tmp/.X11-unix
    environment:
      - PYTHONUNBUFFERED=1
      - DISPLAY=${DISPLAY}
    tty: true
    stdin_open: true
    command: ["bash"]
  </code></pre>
</div>

<h3 id="33-コンテナ内での確認-ubuntu">3.3 コンテナ内での確認 (Ubuntu)</h3>

<ol>
  <li>
    <p>コンテナを起動し、シェルに入ります：</p>
    <div class="code-container">
      <button class="copy-button" onclick="copyCode(this)">Copy</button>
      <pre><code class="language-sh">
docker-compose up -d
docker exec -it kaggle bash
      </code></pre>
    </div>
  </li>
  <li>
    <p>コンテナ内で DISPLAY の値を確認：</p>
    <div class="code-container">
      <button class="copy-button" onclick="copyCode(this)">Copy</button>
      <pre><code class="language-sh">
echo $DISPLAY
      </code></pre>
    </div>
    <p><strong>期待値:</strong> ホストと同じ値（例: <code>:0</code>）</p>
  </li>
  <li>
    <p>X11 アプリ（例: <code>xclock</code>）を起動し、ウィンドウが表示されるか確認します：</p>
    <div class="code-container">
      <button class="copy-button" onclick="copyCode(this)">Copy</button>
      <pre><code class="language-sh">
xclock
      </code></pre>
    </div>
  </li>
</ol>

<hr>

<h2 id="4-よくある問題と対策">4. よくある問題と対策</h2>

<h3 id="41-x11-接続エラー-xclock-エラー">4.1 X11 接続エラー (xclock エラー)</h3>

<p><strong>問題:</strong></p>
<p>Docker コンテナ内で <code>xclock</code> 実行時に <code>Error: Can't open display:</code> が表示される。</p>

<p><strong>対策:</strong></p>
<ul>
  <li>
    <p><strong>ホスト側で DISPLAY の確認と設定</strong><br>
       Mac では <code>export DISPLAY=$(ipconfig getifaddr en0):0</code>（ただし Docker 内には <code>host.docker.internal:0</code> を渡す）</p>
  </li>
  <li>
    <p><strong>xhost の設定</strong><br>
       ホスト側で <code>xhost +local:</code> を実行し、Docker などからの接続を許可する。</p>
  </li>
  <li>
    <p><strong>Docker 起動時の環境変数</strong><br>
       コンテナ起動時に <code>-e DISPLAY=host.docker.internal:0</code>（Mac）または <code>-e DISPLAY=$DISPLAY</code>（Ubuntu）を正しく渡す。</p>
  </li>
</ul>
<p>[詳細はこちら](#41-x11-接続エラー-xclock-エラー) を参照。</p>

<h3 id="42-opencv-の-cvimshow-が動作しない">4.2 OpenCV の cv.imshow が動作しない</h3>

<p><strong>問題:</strong></p>
<p>Docker コンテナ内で <code>cv.imshow</code> を使用すると、以下のエラーが発生する場合がある。<br>
<code>cv2.error: OpenCV(4.11.0) ... The function is not implemented...</code></p>

<p><strong>原因:</strong></p>
<p><code>opencv-python-headless</code> を使用している場合、GUI 表示用の機能が含まれていない。</p>

<p><strong>対策:</strong></p>
<ul>
  <li>
    <p><strong>GUI 表示が必要な場合</strong><br>
       Dockerfile や requirements.txt で <code>opencv-python</code> を使用し、<code>opencv-python-headless</code> は無効にする。<br>
       必要なライブラリ（例: <code>libgtk2.0-dev</code>、<code>pkg-config</code>）がインストールされていることを確認する。</p>
  </li>
  <li>
    <p><strong>ヘッドレスモードで実行する場合</strong><br>
       <code>cv.imshow</code> の代わりに画像をファイルに保存する（例: <code>cv.imwrite</code>）か、Jupyter Notebook などで inline 表示する方法に切り替える。</p>
  </li>
</ul>
<p>[詳細はこちら](#11-dockerfile-の例) を参照。</p>

<hr>

<h2 id="5-参考情報補足">5. 参考情報・補足</h2>

<ul>
  <li>
    <p><strong>XQuartz の再起動と設定変更</strong><br>
       XQuartz の設定変更後は必ず再起動してください。</p>
  </li>
  <li>
    <p><strong>内部リンクを活用</strong><br>
       各問題の詳細対策は本文中のアンカーリンクから参照可能です。<br>
       例えば、X11 接続エラーの詳細は <a href="#41-x11-接続エラー-xclock-エラー">4.1</a> をクリックしてください。</p>
  </li>
  <li>
    <p><strong>Docker Desktop for Mac の注意点</strong><br>
       Mac では <code>network_mode: "host"</code> は正しく動作しないため、DISPLAY を <code>host.docker.internal:0</code> に設定する方法を採用しています。</p>
  </li>
</ul>

<hr>

<p><em>作成日: 2025-02-01</em></p>

<script>
function copyCode(button) {
  const code = button.nextElementSibling.innerText;
  navigator.clipboard.writeText(code).then(function() {
    button.innerText = 'Copied!';
    setTimeout(function() {
      button.innerText = 'Copy';
    }, 2000);
  }).catch(function(error) {
    console.error('Copy failed', error);
  });
}
</script>

</body>
</html>

---

※ このファイル全体をそのまま保存すると、Web ブラウザで表示した場合に各コードブロック上部に「Copy」ボタンが現れます。  
※ Markdown ビューアによっては HTML タグやスクリプトが動作しない場合がありますので、その場合はご利用の環境に合わせて調整してください。
