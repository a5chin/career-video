# Career Video
## Usage
```sh:example
python main.py --base inputs/base.MOV --slide inputs/slide.mov --time 35.0
```

## Dir Structure
```
career-video
├── inputs
│   ├── base.*
│   └── slide.*
└── outputs
    └── work.mp4
```
- `inputs/base.*`
  - 人が映っている画像（こっちの音声を使う）
- `inputs/slide.*`
  - PowerPointの動画
- `outputs/work.mp4`
  - `base.*`と`slide.*`を合成させた動画ファイル
