# ToDoApp_Flask_Vuejs

# ToDoリストのアプリケーション作成

HTTPの仕組みやwebアプリに用いる諸言語の理解を深めるためにtodoアプリの作成した。
用いた言語はFlask, sqlite3, Vue.js, HTML, Bootstrap。

## ディレクトリ構造
```
--- app.py            #サーバーファイル　Flask
|--- sample.sqlite3   #データベースファイル
|--- templates        
|  |--- index.html    #表示用ファイル(HTML, Vue.js)
|  |--- layout.html   #レイアウト
|
|--- static
  |--- style.css      #templates内の見栄えを管理(css)
```

## 最初の画面

<img src="https://user-images.githubusercontent.com/70735561/146554116-c6e951d9-f142-47a2-b439-d19f073710d5.png">

上のテキストボックスに入力してピンクのボタンを押すと、下のimcomplete itemsの欄に追加される。追加された情報はajax経由でデータベースに追加される。

imcomplete itemsの緑のボタンを押すと、隣のcomplete itemsに移る。また、compolete itemsの灰色ボタンを押すとcomplete itemsの欄に戻される。
緑ボタンと灰色ボタンを押した際の情報は逐一データベースに反映される。

また、赤ボタンを押すと表示が消え、データベースからも消去される。
