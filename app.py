import streamlit as st

st.set_page_config(
    page_title="🌈 MBTI 진로 & 포켓몬 추천",
    page_icon="✨",
    layout="centered"
)

# 제목
st.title("🌟 MBTI 진로 & 포켓몬 추천기 🌟")
st.write("💖 나의 MBTI에 어울리는 진로와 포켓몬을 찾아보자!")
st.write("😎 재미로 보는 추천이니까 가볍게 즐겨줘!")

# MBTI 데이터
mbti_data = {
    "INTJ": {
        "careers": [
            {
                "career": "🧠 데이터 사이언티스트",
                "major": "컴퓨터공학과, 통계학과",
                "personality": "논리적이고 분석을 좋아하는 사람!"
            },
            {
                "career": "🏗️ 건축가",
                "major": "건축학과",
                "personality": "창의적이면서 계획 세우기를 좋아하는 성격!"
            }
        ],
        "pokemon": {
            "name": "뮤츠",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/150.png",
            "desc": "🧠 엄청 똑똑하고 전략적인 성격! 혼자 깊게 생각하는 걸 좋아해!"
        }
    },

    "INFP": {
        "careers": [
            {
                "career": "🎨 일러스트레이터",
                "major": "디자인학과",
                "personality": "감성적이고 창의력이 풍부한 사람!"
            },
            {
                "career": "🎬 영화감독",
                "major": "영화영상학과",
                "personality": "자기만의 세계관이 뚜렷한 스타일!"
            }
        ],
        "pokemon": {
            "name": "이브이",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/133.png",
            "desc": "🌸 따뜻하고 감성적인 분위기! 다양한 가능성을 가진 포켓몬!"
        }
    },

    "ENFP": {
        "careers": [
            {
                "career": "📺 유튜버 / 크리에이터",
                "major": "미디어학과",
                "personality": "끼 많고 자유로운 분위기를 좋아하는 사람!"
            },
            {
                "career": "🌍 여행 기획자",
                "major": "관광학과",
                "personality": "새로운 경험을 사랑하는 모험가 타입!"
            }
        ],
        "pokemon": {
            "name": "피카츄",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png",
            "desc": "⚡ 밝고 활발한 분위기의 핵인싸 포켓몬!"
        }
    },

    "ISTJ": {
        "careers": [
            {
                "career": "🏦 회계사",
                "major": "회계학과",
                "personality": "꼼꼼하고 책임감 강한 사람!"
            },
            {
                "career": "👮 경찰관",
                "major": "경찰행정학과",
                "personality": "원칙을 중요하게 생각하는 성격!"
            }
        ],
        "pokemon": {
            "name": "거북왕",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/9.png",
            "desc": "🛡️ 믿음직하고 책임감 있는 든든한 스타일!"
        }
    },

    "ENTP": {
        "careers": [
            {
                "career": "🚀 스타트업 창업가",
                "major": "경영학과",
                "personality": "도전 정신 강하고 새로운 걸 좋아하는 성격!"
            },
            {
                "career": "🎤 마케팅 기획자",
                "major": "광고홍보학과",
                "personality": "아이디어가 넘치고 사람 만나는 걸 좋아하는 타입!"
            }
        ],
        "pokemon": {
            "name": "팬텀",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/94.png",
            "desc": "😈 장난기 많고 창의력이 폭발하는 성격!"
        }
    },

    "INFJ": {
        "careers": [
            {
                "career": "🩺 상담심리사",
                "major": "심리학과",
                "personality": "공감 능력이 뛰어나고 따뜻한 사람!"
            },
            {
                "career": "✍️ 작가",
                "major": "문예창작과",
                "personality": "상상력이 풍부하고 감수성이 깊은 스타일!"
            }
        ],
        "pokemon": {
            "name": "루기아",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/249.png",
            "desc": "🌊 신비롭고 조용하지만 강한 내면을 가진 포켓몬!"
        }
    }
}

# 기본값 추가 (나머지 MBTI용)
default_pokemon = {
    "name": "메타몽",
    "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/132.png",
    "desc": "✨ 어떤 모습으로도 변신 가능한 무한한 가능성의 포켓몬!"
}

# MBTI 리스트
mbti_list = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

# 없는 MBTI 자동 생성
for mbti in mbti_list:
    if mbti not in mbti_data:
        mbti_data[mbti] = {
            "careers": [
                {
                    "career": "💼 다양한 전문 직업",
                    "major": "관련 전공 선택 가능",
                    "personality": "자신의 장점을 살릴 수 있는 성격!"
                },
                {
                    "career": "🌟 창의적인 미래 직업",
                    "major": "관심 분야 학과 추천",
                    "personality": "잠재력이 뛰어난 타입!"
                }
            ],
            "pokemon": default_pokemon
        }

# 선택창
selected_mbti = st.selectbox(
    "👇 MBTI를 선택해줘!",
    mbti_list
)

# 버튼
if st.button("✨ 결과 보기"):
    data = mbti_data[selected_mbti]

    st.success(f"💖 {selected_mbti} 유형 결과가 나왔어!")

    # 진로 추천
    st.header("🎓 추천 진로")

    for idx, item in enumerate(data["careers"], start=1):
        st.markdown(f"""
        ---
        ## {idx}. {item['career']}

        ### 📚 추천 학과
        👉 {item['major']}

        ### 🌈 잘 어울리는 성격
        👉 {item['personality']}
        """)

    # 포켓몬 추천
    st.header("⚡ 너와 닮은 포켓몬!")

    pokemon = data["pokemon"]

    st.image(
        pokemon["image"],
        width=220
    )

    st.subheader(f"🌟 {pokemon['name']}")

    st.write(pokemon["desc"])

    st.balloons()

# 하단 문구
st.markdown("---")
st.caption("💖 MBTI와 포켓몬 추천은 재미로 보는 콘텐츠야! 가장 중요한 건 너만의 매력을 찾는 거 😎✨")
