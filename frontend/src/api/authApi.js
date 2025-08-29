async function basicFetch(url, payload) {
  const res = await fetch(url, payload)
  const body = await res.json()
  return body
}

// export async function signup(context) {
//   const payload = {
//     method: "POST",
//     headers: {
//       "Content-Type": "application/json",
//     },
//     body: JSON.stringify(context)
//   }
//   const body = await basicFetch("http://localhost:80/api/accounts/signup",payload)
//   return body
// }

// export async function login(context) {
//   const payload = {
//     method: "POST",
//     headers: {
//       "Content-Type": "application/json",
//     },
//     body: JSON.stringify(context)
//   }
//   const body = await basicFetch("http://localhost:80/api/accounts/get-token", payload)
//   return body.token
// }

export async function getAds() {
  const payload = {
    method: "GET",
    headers: {
      "Content-Type": "application/json"
    }
  }
  const body = await basicFetch("http://localhost:80/api/ads", payload)
  // console.log('body: ', body)
  return body
}

export async function getCars() {
  const payload = {
    method: "GET",
    headers: {
      "Content-Type": "application/json"
    }
  }
  const body = await basicFetch("http://localhost:80/api/cars", payload)
  console.log('body: ', body)
  return body
}

export async function getModels() {
  const payload = {
    method: "GET",
    headers: {
      "Content-Type": "application/json"
    }
  }
  const body = await basicFetch("http://localhost:80/api/models", payload)
  // console.log('body: ', body)
  return body
}

export async function getUsers() {
  const payload = {
    method: "GET",
    headers: {
      "Content-Type": "application/json"
    }
  }
  const body = await basicFetch("http://localhost:80/api/users", payload)
  // console.log('body: ', body)
  return body
}

export async function getProfiles() {
  const payload = {
    method: "GET",
    headers: {
      "Content-Type": "application/json"
    }
  }
  const body = await basicFetch("http://localhost:80/api/profiles", payload)
  console.log('body: ', body)
  return body
}