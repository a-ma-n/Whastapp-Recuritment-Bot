const studentCollections = {}                    
let currentCount = 0                    
function leftPad (str, max) {
  str = str.toString();
  return str.length < max ? leftPad("0" + str, max) : str;
}
const scrapeMe = async ()=>{

  while(currentCount<3000){
    currentCount+=10
    const data = await fetch("https://teams.microsoft.com/api/mt/amer/beta/users/searchV2?includeDLs=false&includeBots=true&enableGuest=true&source=searchResults&skypeTeamsInfo=true", {
        "headers": {
            "accept": "application/json, text/plain, */*",
            "accept-language": "en-US,en;q=0.9",
            "authorization": "Bearer eyJ0eXAiOiJKV1QiLCJub25jZSI6ImRfVElZNHpCc0dmNko0eTNuZURFbnRlRUZ2VFNFNXlsWEVXZ2dqdFhPSFkiLCJhbGciOiJSUzI1NiIsIng1dCI6ImtnMkxZczJUMENUaklmajRydDZKSXluZW4zOCIsImtpZCI6ImtnMkxZczJUMENUaklmajRydDZKSXluZW4zOCJ9.eyJhdWQiOiJodHRwczovL2FwaS5zcGFjZXMuc2t5cGUuY29tIiwiaXNzIjoiaHR0cHM6Ly9zdHMud2luZG93cy5uZXQvZDQ5NjNjZTItYWY5NC00MTIyLTk1YTktNjQ0ZThiMDE2MjRkLyIsImlhdCI6MTYwNzc3MTI3MywibmJmIjoxNjA3NzcxMjczLCJleHAiOjE2MDc3Nzg3NzMsImFjY3QiOjAsImFjciI6IjEiLCJhaW8iOiJFMlJnWUdEdTRPeVZDZittRzN4ZWxhK1FjM0ZCb2UyMzVLK1RDNDVIdi8vYXpCeXIydzRBIiwiYW1yIjpbInB3ZCJdLCJhcHBpZCI6IjVlM2NlNmMwLTJiMWYtNDI4NS04ZDRiLTc1ZWU3ODc4NzM0NiIsImFwcGlkYWNyIjoiMCIsImF1dGhfdGltZSI6MTYwNzY5MjM4NCwiZmFtaWx5X25hbWUiOiIxOUJDQjAwMTEiLCJnaXZlbl9uYW1lIjoiU0FNQVJUSFlBIEpIQSIsImlwYWRkciI6IjQ3LjguMjUuMSIsIm5hbWUiOiJTQU1BUlRIWUEgSkhBIiwib2lkIjoiNmY1ZDE1Y2YtNzcwOS00ZTQzLTlmODktNWEyYzVjZTRlMDAzIiwicHVpZCI6IjEwMDMyMDAwQjg1RjIwMzQiLCJyaCI6IjAuQVRjQTRqeVcxSlN2SWtHVnFXUk9pd0ZpVGNEbVBGNGZLNFZDalV0MTduaDRjMFkzQUowLiIsInNjcCI6InVzZXJfaW1wZXJzb25hdGlvbiIsInNpZ25pbl9zdGF0ZSI6WyJrbXNpIl0sInN1YiI6ImtfNUdiMERnX1c0VktPQUpPak5USjdGay1jN0JsRi1pMHJoOWxCYUJqVXciLCJ0aWQiOiJkNDk2M2NlMi1hZjk0LTQxMjItOTVhOS02NDRlOGIwMTYyNGQiLCJ1bmlxdWVfbmFtZSI6InNhbWFydGh5YS5qaGEyMDE5QHZpdHN0dWRlbnQuYWMuaW4iLCJ1cG4iOiJzYW1hcnRoeWEuamhhMjAxOUB2aXRzdHVkZW50LmFjLmluIiwidXRpIjoiNVk5bHkxSG5xMENlWkxhYTNSVVZBUSIsInZlciI6IjEuMCIsIndpZHMiOlsiYjc5ZmJmNGQtM2VmOS00Njg5LTgxNDMtNzZiMTk0ZTg1NTA5Il19.FHxhxBme1n7JRN_IGQ-MIKXsBRUFPPmzZ7o-BixGpI6DdZfN9ASPAhrLhbIawcunZnTz3jbIgIKcfeNsT_tALB1zYRne2jbPrgsQnKbwrGI3CKLhDLZRm46oE93dC_LN7mY8Z09X20ux7-R8jCiorpTR-3_dYZhQVmR0WGAhHivxRrc_MIgcowINhUQDjXwe6vSbMKfRV7nxFeMvXuyX83cRkZD2qsLEze_ErRZjb7JGV41lD9KTYajr3VPyCik1CgwneIHbKBgZyQKoJtbcpPyraQ4CQps7TGSlCLdDnqCOUvwS7kAjLHmQlWxwlQtQ1ImByTfyhndDoQYAk2CXPg",
            "content-type": "application/json",
            "sec-ch-ua": "\"Google Chrome\";v=\"87\", \" Not;A Brand\";v=\"99\", \"Chromium\";v=\"87\"",
            "sec-ch-ua-mobile": "?0",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "x-anchormailbox": "samarthya.jha2019@vitstudent.ac.in",
            "x-ms-client-cpm": "ApplicationLaunch",
            "x-ms-client-env": "pckgsvc-prod-c2-asse-01",
            "x-ms-client-type": "web",
            "x-ms-client-version": "1415/1.0.0.2020120223",
            "x-ms-scenario-id": "354",
            "x-ms-serp-correlation-id": "fd06af21-739c-4821-a9a5-1635f254c6d0",
            "x-ms-session-id": "d6e29343-156a-96f3-c270-51c8e4fa0f01",
            "x-ms-user-type": "null",
            "x-ringoverride": "general",
            "x-skypetoken": "eyJhbGciOiJSUzI1NiIsImtpZCI6IjEwMiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE2MDc3NzE1NzMsImV4cCI6MTYwNzg1Nzk3Mywic2t5cGVpZCI6Im9yZ2lkOjZmNWQxNWNmLTc3MDktNGU0My05Zjg5LTVhMmM1Y2U0ZTAwMyIsInNjcCI6NzgwLCJjc2kiOiIxNjA3NzcxMjczIiwidGlkIjoiZDQ5NjNjZTItYWY5NC00MTIyLTk1YTktNjQ0ZThiMDE2MjRkIiwicmduIjoiYW1lciJ9.knF4UIzX8B603hPuUdAh5DflNNY31QNeY6KXDkpgBXHyizICuoMH0P3dnVb87_qk6ttJyy4zyKYq_ve0TFft_3_t4GNe6ENpAZiI1_ePt8Ze4ALIL31-AQKcE5NTqEPdgrSH2gqGVLcpC5WukiDalyXGg23ihXBoigGsJdkHSbqOjyfwdDUR6vkU40pycWiQ9vzImaVtAATX3hvIuGx35QuPuBKZN5kLPyba3HNR1W1priLrIp8xVIAxFVJ52JG0Hn89nXK7xTgmDSeKPUMwobNCB7goyH2jr0GI0JFjPjNMPDdAtVIOZ5sMswotinWMP456DkV4LrKMeOhJ9hamnA"
          },
      "referrer": "https://teams.microsoft.com/_?",
      "referrerPolicy": "strict-origin-when-cross-origin",
      "body": `20BIT${leftPad(currentCount,4)}`,
      "method": "POST",
      "mode": "cors",
      "credentials": "include"
    });
    const resp  = await data.json()
    resp.value.forEach(person=>{
      try{
        const {mail,phones} = person
        studentCollections[person.userLocation] ={mail,phone:  phones[0].number}
      }
      catch(e){

      }
    })
    console.log(JSON.stringify(studentCollections))
  }
}

scrapeMe()