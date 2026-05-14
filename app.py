import streamlit as st

st.set_page_config(
    page_title="✨ MBTI 진로 추천",
    page_icon="💼",
    layout="centered"
)

st.title("🌈 MBTI 기반 진로 추천 서비스")
st.subheader("🔍 나의 MBTI로 어울리는 진로를 찾아보자!")
st.write("MBTI를 선택하면 ✨ 찰떡같이 어울리는 진로 2가지를 추천해줄게 😎")

# MBTI별 데이터
mbti_data = {
    "INTJ": [
        {
            "career": "🧠 데이터 사이언티스트",
            "major": "컴퓨터공학과, 통계학과",
            "personality": "논리적이고 분석을 좋아하는 사람에게 딱!"
        },
        {
            "career": "🏗️ 건축가",
            "major": "건축학과",
            "personality": "창의적이면서 계획 세우기를 좋아하는 성격!"
        }
    ],

    "INTP": [
        {
            "career": "💻 프로그래머",
            "major": "소프트웨어학과, 컴퓨터공학과",
            "personality": "호기심 많고 문제 해결을 좋아하는 사람!"
        },
        {
            "career": "🔬 연구원",
            "major": "물리학과, 화학과",
            "personality": "깊게 탐구하는 걸 즐기는 스타일!"
        }
    ],

    "ENTJ": [
        {
            "career": "📈 CEO / 경영인",
            "major": "경영학과",
            "personality": "리더십 있고 추진력이 강한 사람!"
        },
        {
            "career": "⚖️ 변호사",
            "major": "법학과",
            "personality": "논리적으로 말 잘하고 목표 지향적인 성격!"
        }
    ],

    "ENTP": [
        {
            "career": "🎤 마케팅 기획자",
            "major": "광고홍보학과",
            "personality": "아이디어가 넘치고 사람 만나는 걸 좋아하는 타입!"
        },
        {
            "career": "🚀 스타트업 창업가",
            "major": "창업학과, 경영학과",
            "personality": "도전 정신 강하고 새로운 걸 좋아하는 성격!"
        }
    ],

    "INFJ": [
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

    "INFP": [
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

    "ENFJ": [
        {
            "career": "👩‍🏫 교사",
            "major": "교육학과",
            "personality": "사람을 이끄는 걸 좋아하고 배려심 많은 성격!"
        },
        {
            "career": "🎙️ 아나운서",
            "major": "언론정보학과",
            "personality": "소통 능력이 뛰어나고 밝은 에너지!"
        }
    ],

    "ENFP": [
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

    "ISTJ": [
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

    "ISFJ": [
        {
            "career": "💉 간호사",
            "major": "간호학과",
            "personality": "배려심 많고 성실한 사람에게 추천!"
        },
        {
            "career": "🏫 사회복지사",
            "major": "사회복지학과",
            "personality": "남을 돕는 데 보람을 느끼는 타입!"
        }
    ],

    "ESTJ": [
        {
            "career": "📋 공무원",
            "major": "행정학과",
            "personality": "체계적이고 책임감이 강한 스타일!"
        },
        {
            "career": "🏢 프로젝트 매니저",
            "major": "경영학과",
            "personality": "조직 관리와 리더 역할을 잘하는 사람!"
        }
    ],

    "ESFJ": [
        {
            "career": "🎉 이벤트 플래너",
            "major": "호텔관광학과",
            "personality": "사람들과 어울리는 걸 좋아하는 성격!"
        },
        {
            "career": "🧑‍⚕️ 의료 코디네이터",
            "major": "보건행정학과",
            "personality": "친절하고 세심한 사람에게 잘 맞아!"
        }
    ],

    "ISTP": [
        {
            "career": "🔧 엔지니어",
            "major": "기계공학과",
            "personality": "손으로 만드는 걸 좋아하는 실전형 스타일!"
        },
        {
            "career": "🚗 자동차 정비사",
            "major": "자동차공학과",
            "personality": "기계 다루는 걸 즐기는 사람!"
        }
    ],

    "ISFP": [
        {
            "career": "📸 사진작가",
            "major": "사진영상학과",
            "personality": "감각적이고 예술적인 분위기의 사람!"
        },
        {
            "career": "💄 메이크업 아티스트",
            "major": "뷰티미용학과",
            "personality": "섬세하고 트렌드에 민감한 스타일!"
        }
    ],

    "ESTP": [
        {
            "career": "⚽ 스포츠 코치",
            "major": "체육학과",
            "personality": "활동적이고 에너지 넘치는 사람!"
        },
        {
            "career": "💼 영업 전문가",
            "major": "마케팅학과",
            "personality": "사람들과 소통하는 걸 즐기는 타입!"
        }
    ],

    "ESFP": [
        {
            "career": "🎭 배우",
            "major": "연극영화과",
            "personality": "사람들 앞에서 빛나는 걸 좋아하는 성격!"
        },
        {
            "career": "🎤 아이돌 / 가수",
            "major": "실용음악과",
            "personality": "흥 많고 표현력이 뛰어난 스타일!"
        }
    ]
}

# MBTI 선택
mbti = st.selectbox(
    "👇 너의 MBTI를 선택해줘!",
    list(mbti_data.keys())
)

# 버튼
if st.button("✨ 진로 추천 받기"):
    st.success(f"💖 {mbti} 유형에게 추천하는 진로야!")

    for idx, item in enumerate(mbti_data[mbti], start=1):
        st.markdown(f"""
        ---
        ## {idx}. {item['career']}

        ### 🎓 추천 학과
        👉 {item['major']}

        ### 🌟 이런 성격에게 잘 어울려!
        👉 {item['personality']}
        """)

    st.balloons()

st.markdown("---")
st.caption("🌈 MBTI는 참고용일 뿐! 가장 중요한 건 네가 좋아하는 일을 찾는 거야 😎")
