# AnalyzingSound  


最近、映像をちまちま作っている。  

映像と音を同期させた映像を作りたいとか思ったりするので、とりあえず調べる。  


---  


### 音と同期した映像の作り方

(1) 周波数解析（スペクトラム解析？）的なものを噛ませて、それが映像のパラメータになるようにする  
- なんかコードを書く必要がある  
- Python でも解析が出来るぽいのでそれでなんとかするかも  
  - Blender（じゃなくても、プリレンダリング系）でやるなら、フレームレートを設定（30 or 24）して、 CSV にまとめて書き出して、キーフレームに打ち込ませる（かな）  
    - フレームレートっていう概念て、どうやるかな？？    
    - Blender-Python で、Pandas 使えれば、この CSV のデータからキーフレーム打ちは、秒で出来る   
  - 描画を Python でやるにも、PIL や、OpenCV で描画でフレーム落ちする可能性があるので、一旦 CSV にするのが、多分、吉  
- 音全域で、全部処理されるものを、捨てるところ捨てて、うまく料理しないとけない気がするのでその辺はやってみて...  
  ![photo](ex/Spectrum_ex.png)  


(2) 手でキーフレームを打つ時に、音に合わせて設定する  
- 面倒臭い  
- 取捨選択をしないといけない。センス大事？耳も大事？  
- 普通に面倒臭い  



----  


### Ref.  

Pythonで科学計算ライブラリ「numpy」を用いて周波数解析(tomosoft)  
[https://tomosoft.jp/design/?p=11527](https://tomosoft.jp/design/?p=11527)  

Pythonを使って音声データからスペクトログラムを作成する(自調自考の旅)  
[https://own-search-and-study.xyz/2017/10/27/python%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%A6%E9%9F%B3%E5%A3%B0%E3%83%87%E3%83%BC%E3%82%BF%E3%81%8B%E3%82%89%E3%82%B9%E3%83%9A%E3%82%AF%E3%83%88%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%A0%E3%82%92%E4%BD%9C/](https://own-search-and-study.xyz/2017/10/27/python%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%A6%E9%9F%B3%E5%A3%B0%E3%83%87%E3%83%BC%E3%82%BF%E3%81%8B%E3%82%89%E3%82%B9%E3%83%9A%E3%82%AF%E3%83%88%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%A0%E3%82%92%E4%BD%9C/)  

Pythonで音の高速フーリエ変換（FFT）  
[http://denshi.blog.jp/signal_processing/python/fft](http://denshi.blog.jp/signal_processing/python/fft)  

【Python】WAVファイルの波形データにFFTかけて周波数スペクトルを複数表示する【サウンドプログラミング】  
[http://tacky0612.hatenablog.com/entry/2017/12/12/174405](http://tacky0612.hatenablog.com/entry/2017/12/12/174405)  

