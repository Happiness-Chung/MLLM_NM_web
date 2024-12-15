document.getElementById('send-button').addEventListener('click', async () => {
    const userInput = document.getElementById('user-input').value;
    const imageFile = document.getElementById('image-upload').files[0]; // 이미지 파일 가져오기
    const chatBox = document.getElementById('chat-box');
  
    if (!userInput.trim() && !imageFile) {
      alert('Please provide either a prompt or an image.');
      return;
    }
  
    // FormData 객체 생성
    const formData = new FormData();
    formData.append('input', userInput); // 프롬프트 텍스트 추가
    if (imageFile) formData.append('image', imageFile); // 이미지 파일 추가
  
    // API 호출
    try {
      const response = await fetch('http://localhost:8000/api/process_input/', {
        method: 'POST',
        body: formData, // FormData 객체 전송
      });
  
      const data = await response.json();
      chatBox.innerHTML += `<div>LLaVA-NM: ${data.output}</div>`;
      chatBox.scrollTop = chatBox.scrollHeight; // 스크롤 최신 메시지로 이동
    } catch (error) {
        console.error('Error:', error);
        chatBox.innerHTML += `<div>LLaVA-NM: Error occurred. ${error.message}</div>`;
      }
  });
  