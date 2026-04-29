import api from './client';

export interface AdminUser {
  id: number;
  username: string;
  email: string;
  is_active: boolean;
  is_staff: boolean;
  date_joined: string;
  contact: {
    display_name: string;
    email: string;
    companyWebsite: string;
    primaryBusinessAddress: string;
  } | null;
}

export interface AdminUserAllData {
  user: {
    id: number;
    username: string;
    email: string;
    is_active: boolean;
  };
  steps: Record<string, Record<string, unknown> | null>;
}

export async function getAdminUsers(): Promise<AdminUser[]> {
  const { data } = await api.get<AdminUser[]>('admin/users');
  return data;
}

export async function createAdminUser(payload: {
  username: string;
  email: string;
  password: string;
}): Promise<{ id: number; username: string; email: string }> {
  const { data } = await api.post('admin/users', payload);
  return data;
}

export async function activateUser(userId: number): Promise<void> {
  await api.post(`admin/users/${userId}/activate`);
}

export async function getAdminUserData(
  userId: number
): Promise<AdminUserAllData> {
  const { data } = await api.get<AdminUserAllData>(
    `admin/users/${userId}/data`
  );
  return data;
}

export async function postAdminUserStepData(
  userId: number,
  stepKey: string,
  payload: Record<string, unknown>
): Promise<Record<string, unknown>> {
  const { data } = await api.post(
    `admin/users/${userId}/data/${stepKey}`,
    payload
  );
  return data;
}

export async function getAdminMatchPDF(userId: number): Promise<Blob> {
  const { data } = await api.get<Blob>(
    `admin/users/${userId}/match-pdf`,
    { responseType: 'blob' }
  );
  return data;
}
