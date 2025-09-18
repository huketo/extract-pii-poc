# Extract PII by LangExtract

[LangExtract](https://github.com/google/langextract) 를 사용하여 텍스트에서 PII(개인 식별 정보)를 추출하는 예제입니다.

## 개요

전통적으로 PII 추출은 정규 표현식이나 규칙 기반 접근 방식을 사용하여 수행되었습니다. 그러나 이러한 방법은 유지 관리가 어렵고 새로운 유형의 PII를 식별하는 데 한계가 있습니다. 이후 머신러닝 모델을 사용한 접근 방식이 도입되었습니다. 이 당시에는 _Encoder-Only_ 모델(예: BERT)이 주로 사용되었습니다. 최근에는 GPT 같은 Transformer 기반의 _Encoder-Decoder_ 모델이 급격하게 발전하면서 데이터 라벨링과 모델 훈련에 대한 의존도를 줄이고, 프롬프트 엔지니어링을 통해 PII 추출 작업을 수행하는 방법이 주목받고 있습니다.

그러한 배경에서 Google은 **LangExtract** 라는 오픈소스 프로젝트를 발표했습니다. **LangExtract**는 Gemini 같은 **LLM(대형 언어 모델)** 을 활용하여 대량의 비정형 텍스트를 구조화된 정보로 처리하기 위해서 개발된 도구입니다.

이 예제에서는 **LangExtract**를 사용하여 텍스트에서 PII를 추출하는 방법을 보여줍니다.

또한 본 예제에는 개인 식별 정보(PII)를 대상으로 하고 있으므로, 실제 데이터가 아닌 샘플 데이터를 사용합니다.
이러한 개인 식별 정보(PII) 유출을 방지하기 위해, 본 예제는 로컬에서 실행되는 Ollama에서 Google의 `gemma3:4b` 모델을 사용합니다.

## PII List (PII 목록)

1. Name / 이름
2. Name Family / 성
3. Name Given / 이름(성 제외)
4. Age / 나이
5. Date of Birth / 생년월일
6. Gender / 성별
7. Sexuality / 성적 지향
8. Marital Status / 결혼 여부
9. Phisical Attributes / 신체적 특징
10. Zodiac Sign / 별자리
11. Social Security Number / 주민등록번호
12. Driver's License Number / 운전면허증 번호
13. Passport Number / 여권 번호
14. Health Insurance Number / 건강보험 번호
15. Vehicle ID / 차량 식별 번호
16. Account Number / 계좌 번호
17. Numeric PII / 숫자형 PII
18. Email Address / 이메일 주소
19. Phone Number / 전화번호
20. Location / 위치
21. Location Address / 주소
22. Location Address Street / 도로명 주소
23. Location City / 시
24. Location State / 주 or 도
25. Location Country / 국가
26. Location Zip Code / 우편번호
27. Location Coordinates / 좌표
28. IP Address / IP 주소
29. URL / 웹사이트 주소
30. Username / 사용자 이름
31. Password / 비밀번호
32. File name / 파일 이름
33. Occupation / 직업
34. Organization / 조직
35. Organization Medical Facility / 의료 기관
36. Name Medical Professional / 의료 전문가 이름
37. Origin / 출신
38. Language / 언어
39. Political Affiliation / 정치 성향
40. Religion / 종교
41. Date / 날짜
42. Date Interval / 기간
43. Time / 시간
44. Duration / 지속 시간
45. Event / 이벤트
46. Price / 금액

## 사전 준비

- [uv](https://github.com/astral-sh/uv)
- [ollama](https://ollama.com/download)

## 설치

```shell
uv sync
```

## 사용법

## Jupyter 노트북에서 실행

1. `extract_pii_poc.ipynb` 노트북을 엽니다.
2. 커널 선택: Windows의 경우 `.venv\Scripts\python.exe` , macOS/Linux의 경우 `.venv/bin/python`을 선택합니다.
3. 노트북을 실행하여 PII 추출을 확인합니다. 

## 커맨드 라인에서 실행

```shell
uv run main.py
```

실행결과는 `extracted_pii_results.jsonl` 파일과 `extracted_pii_visualization.html` 파일로 저장됩니다.

### Extract 설정 변경

```python
# Extract PII from the sample text using the defined prompt and examples
result = lx.extract(
    text_or_documents=sample_text,
    prompt_description=prompt_description,
    examples=examples,
    model_id="gemma3:4b",
    model_url="http://localhost:11434",
    # extraction_passes=3,  # Improves recall through multiple passes
    # max_workers=10,  # Parallel processing for speed
    # max_char_buffer=1000,  # Smaller contexts for better accuracy
)
```

이 부분에서 `extraction_passes`, `max_workers`, `max_char_buffer` 등의 설정을 변경하여 추출 성능을 조정할 수 있습니다.

- `extraction_passes`: 추출 작업을 여러 번 수행하여 재현성을 높입니다.
- `max_workers`: 병렬 처리에 사용할 워커 수를 지정합니다.
- `max_char_buffer`: 적은 컨텍스트가 더 나은 정확도를 제공할 수 있습니다.

설정 조정 전에는 Entities는 **18**개 -> 설정 조정 후에는 Entities는 **21**개로 추출되었습니다.

실행된 보고서는 ![여기](https://huketo.github.io/extract-pii-poc)에서 확인 가능합니다.
