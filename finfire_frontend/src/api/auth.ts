import api from './client';
import type {
  LoginResponse,
  RegisterPayload,
  User,
  PasswordResetRequest,
  PasswordResetConfirm,
} from '../types/api';

export async function login(
  username: string,
  password: string
): Promise<LoginResponse> {
  const { data } = await api.post<LoginResponse>('auth/token/login/', {
    username,
    password,
  });
  return data;
}

export async function logout(): Promise<void> {
  await api.post('auth/token/logout/');
}

export async function register(
  username: string,
  email: string,
  password: string
): Promise<User> {
  const payload: RegisterPayload = { username, email, password };
  const { data } = await api.post<User>('auth/users/', payload);
  return data;
}

export async function getCurrentUser(): Promise<User> {
  const { data } = await api.get<User>('auth/users/me/');
  return data;
}

export async function updateProfile(
  payload: Partial<User>
): Promise<User> {
  const { data } = await api.patch<User>('auth/users/me/', payload);
  return data;
}

export async function requestPasswordReset(
  email: string
): Promise<void> {
  const payload: PasswordResetRequest = { email };
  await api.post('auth/password/reset/', payload);
}

export async function confirmPasswordReset(
  payload: PasswordResetConfirm
): Promise<void> {
  await api.post('auth/password/reset/confirm/', payload);
}

export async function activateAccount(
  uid: string,
  token: string
): Promise<void> {
  await api.post('auth/users/activation/', { uid, token });
}
