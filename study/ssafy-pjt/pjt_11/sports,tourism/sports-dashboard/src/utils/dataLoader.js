// sports.jsonl 파일을 불러와서 파싱하는 유틸 함수

export async function loadSportsData() {
  const response = await fetch('/src/data/sports.jsonl')
  const text = await response.text()

  // JSONL은 줄마다 JSON 객체가 있는 형식이에요
  const lines = text.trim().split('\n')
  const data = lines.map(line => JSON.parse(line))

  return data
}

export async function loadTourismData() {
  const response = await fetch('/src/data/travel_tourism.jsonl')
  const text = await response.text()
  const lines = text.trim().split('\n')
  return lines.map(line => JSON.parse(line))
}