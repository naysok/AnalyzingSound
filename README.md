# AnalyzingSound  


最近、映像をちまちま作っている。  

映像と音を同期させた映像を作りたいとか思ったりするので、とりあえず調べる。  


---  


### 音と同期した映像の作り方

(1) 周波数解析（Frequency Spectrum, スペクトラム解析？）的なものを噛ませて、それが映像のパラメータになるようにする  
- なんかコードを書く必要がある  
- Python でも解析が出来るぽいのでそれでなんとかする  
  - Python には、.wav 形式の音声ファイルを扱う wave ライブラリがあるので、それで。mp3 → wav は ffmpeg でできる。  
  - Blender（じゃなくても、プリレンダリング系）でやるなら、フレームレートを設定（30 or 24）して、 CSV にまとめて書き出して、キーフレームに打ち込ませる（かな）  
    - Python でフレームレートっていう概念をどうやるかな？？    
    - Blender-Python で、Pandas 使えれば、この CSV のデータからキーフレーム打ちは、秒で出来る   
  - 描画を Python でやるにも、PIL や、OpenCV で描画でフレーム落ちする可能性があるので、一旦 CSV にするのが、多分、吉  
- 音全域で、全部処理されるものを、捨てるところ捨てて、うまく料理しないとけない気がするのでその辺はやってみて...  
  ![photo](ex/Spectrum_ex.png)  


(2) 手でキーフレームを打つ時に、音に合わせて設定する  
- 面倒臭い  
- 取捨選択をしないといけない。センス大事？耳も大事？  
- 普通に面倒臭い  


---  


### 音声ファイルについて  

print_info.py で出力される結果例  

```python
# Channel : 2
# Width : 2
# Frame Rate : 44100
# Frame num :  9176832
# Tatal Time : 208.09142857142857
# Total Time : 3 min 28.091428571428565 sec
```

44.1kHz  

1 秒間に 44100 回サンプルを取る  
これで音の上限周波数が決まります。サンプリング周波数の半分の周波数まで記録出来ます。  



----  


### Ref.  


22.4. wave — WAVファイルの読み書き  
[https://docs.python.jp/3/library/wave.html](https://docs.python.jp/3/library/wave.html)  

Pythonで科学計算ライブラリ「numpy」を用いて周波数解析(tomosoft)  
[https://tomosoft.jp/design/?p=11527](https://tomosoft.jp/design/?p=11527)  

Pythonを使って音声データからスペクトログラムを作成する(自調自考の旅)  
[https://own-search-and-study.xyz/2017/10/27/python%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%A6%E9%9F%B3%E5%A3%B0%E3%83%87%E3%83%BC%E3%82%BF%E3%81%8B%E3%82%89%E3%82%B9%E3%83%9A%E3%82%AF%E3%83%88%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%A0%E3%82%92%E4%BD%9C/](https://own-search-and-study.xyz/2017/10/27/python%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%A6%E9%9F%B3%E5%A3%B0%E3%83%87%E3%83%BC%E3%82%BF%E3%81%8B%E3%82%89%E3%82%B9%E3%83%9A%E3%82%AF%E3%83%88%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%A0%E3%82%92%E4%BD%9C/)  

Pythonで音の高速フーリエ変換（FFT）  
[http://denshi.blog.jp/signal_processing/python/fft](http://denshi.blog.jp/signal_processing/python/fft)  

【Python】WAVファイルを等間隔に分割するプログラム【サウンドプログラミング】  
[http://tacky0612.hatenablog.com/entry/2017/11/21/164409](http://tacky0612.hatenablog.com/entry/2017/11/21/164409)  

【Python】複数のWAVファイルの波形を表示するプログラム【サウンドプログラミング】  
[http://tacky0612.hatenablog.com/entry/2017/11/28/133103](http://tacky0612.hatenablog.com/entry/2017/11/28/133103)

【Python】WAVファイルの波形データにFFTかけて周波数スペクトルを複数表示する【サウンドプログラミング】  
[http://tacky0612.hatenablog.com/entry/2017/12/12/174405](http://tacky0612.hatenablog.com/entry/2017/12/12/174405)  

PythonのWaveモジュールを使ってwavファイルを編集する（Qiita）  
情報を表示  
[https://qiita.com/niisan-tokyo/items/d25dada3fa9903862260](https://qiita.com/niisan-tokyo/items/d25dada3fa9903862260)  



